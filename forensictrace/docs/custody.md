# Evidence integrity and chain of custody

Every run now writes tamper-evident evidence (schema 3). The study's experiments keep the
original schema 2 format through `--baseline-format`, so their published storage and time
figures stay reproducible.

## What each run produces

| File | Purpose |
|---|---|
| `run.json` | Evidence: session header, and events with `event_uid`, `ts_wall`, `prev_hash`, `event_hash` |
| `run.json.sha256` | SHA-256 sidecar, unchanged (`sha256sum -c` still works) |
| `run.json.manifest.json` | Binds the file hash, event count, chain ends and report hash to the session |
| `run.json.manifest.sig` | Detached Ed25519 signature over the manifest bytes (with `--sign-key`) |
| `run.json.audit.jsonl` | Hash-chained log of generation, verification and export |

## Commands

```bash
make keys                     # creates ~/.config/forensictrace/investigator.key and .pub
KEY=~/.config/forensictrace/investigator.key

./forensictrace --config C --output cases/run.json --report cases/run.md \
    --investigator "A. Analyst" --case CASE-042 --sign-key $KEY -- bash suspicious.sh

./forensictrace verify cases/run.json --pubkey $KEY.pub     # exit 0 intact, 1 failed, 2 could not run
./forensictrace verify cases/run.json --pubkey $KEY.pub --json --no-audit
./forensictrace export cases/run.json --to /media/usb/CASE-042 --pubkey $KEY.pub

# Independent of ForensicTrace:
openssl pkeyutl -verify -pubin -inkey $KEY.pub -rawin \
    -in cases/run.json.manifest.json -sigfile cases/run.json.manifest.sig
```

Run `python3 tests/test_custody.py` to watch each attack below being caught.

## What verification reports

| Status | Meaning |
|---|---|
| `verified_signed_pinned` | Everything checks out and the manifest was signed by the key you pinned with `--pubkey` |
| `verified_signed_unpinned` | Intact, and the signature matches the key inside the manifest. This does not prove who signed |
| `verified_unsigned` | Internally consistent, but no signature. Someone able to rewrite every file would go unnoticed |
| `legacy_sidecar_ok` | Schema 2 evidence: only the sidecar could be checked |
| `failed` | A problem was found; each one is listed |

Findings name the record concerned where that is possible:

| Attack | Reported as |
|---|---|
| One field of one event edited | `record_modified`, naming that event |
| Event deleted | `record_missing` naming it, plus `chain_break` at the next event |
| Tail cut off | `record_missing` naming the range (the count comes from the manifest) |
| Events reordered or duplicated | `record_out_of_order`, `record_duplicate` |
| Investigator, case or run summary edited | `header_modified` |
| Duplicate JSON key to show one value and hash another | `record_modified` (the last key wins, as in every reader) |
| File, sidecar and the entire chain recomputed | `chain_rewritten`: the chain is consistent but disagrees with the signed manifest |
| All of that, plus the manifest re-signed with the attacker's key | `signature_invalid` under the pinned key |
| Signature removed | `signature_missing` under the pinned key |
| Disguised as schema 2, custody files deleted | fails under the pinned key |
| Manifest, report or audit log edited or deleted | `manifest_missing`, `report_modified`, `audit_broken`, `audit_missing` |

This closes the gap stated in the original report, where rewriting both the file and its
sidecar went undetected.

## Hash format

Hashes are SHA-256, lowercase hex. Fields are hashed by value, not by JSON layout. Each is
`name=<byte length>:<value>\n`, so one value can never run into the next. `null`, `true` and
numbers are hashed as their JSON text.

```
genesis     = SHA-256("ForensicTrace-chain-v1\n" + fields(header))
event_hash  = SHA-256(prev_hash + "\n" + fields(event))      prev_hash of event 1 = genesis
entry_hash  = SHA-256(prev_hash + "\n" + fields(audit))      prev_hash of entry 1 = "ForensicTrace-audit-v1"

header : session_id case_id investigator os_user hostname kernel scenario command config
         collection_mode started_utc finished_utc event_count raw_event_count
         dropped_failed_exec truncated untraced_processes
event  : event_uid id ts_ns ts_wall type syscall pid ppid uid exe target detail ret
         parent_event resource_event
audit  : seq ts_utc action session_id investigator os_user evidence_sha256 outcome detail
```

`tests/test_custody.py` recomputes the chain from this description in Python, with no C code
involved. The key fingerprint is the SHA-256 of the 32 raw public key bytes.

## Measured cost

Measured on the test laptop on 11 November 2026: each of the four study scenarios was run three
times in both formats under configurations C and D, ptrace mode (12 pairs per configuration):

| Config | Mean events | Extra storage | Extra per event | Chain time, mean (max) | Per event |
|---|---|---|---|---|---|
| C | 841 | +78% (77 to 78%) | 293 B | 3.7 ms (8.7) | 4.1 µs |
| D | 2,448 | +85% (85 to 86%) | 292 B | 9.1 ms (15.5) | 3.7 µs |

The extra storage is almost all hashes and identifiers. Hashing runs after the resource capture,
so it is not charged to the workload metrics. Verifying one file, including process start, took
19 ms on average (maximum 41 ms) over 24 files of 841 to 2,448 events. These are small samples on
one machine, indicative only. The same figures are in the technical report, section 4.

## What this does not protect against

- **A compromised private key.** Whoever holds it can sign anything. Keep it off the machine
  under investigation. In the default local setup it is on the same disk, which is convenient
  for a lab and weak against an attacker with that user's access.
- **An unpinned verifier.** Without `--pubkey`, an attacker can re-sign with their own key.
  The result then says `verified_signed_unpinned`, which is why that status is a warning.
- **Tampering before sealing.** The chain is computed when the run ends, not per syscall. An
  attacker controlling the tracer during the run could alter events before they are hashed.
- **Locating a change after a full rewrite.** `chain_rewritten` proves that records changed
  but cannot say which ones, because only the chain ends are signed.
- **Audit log tail removal.** The log is hash-chained but not signed, so deleting the newest
  entries, or rewriting the log entirely, is not detected. Copy it off the machine to protect it.
- **Clock manipulation.** `ts_wall` comes from the system clock. There is no trusted timestamp
  authority (RFC 3161), so the signature proves who signed, not when.
- **Identity.** `--investigator` is whatever the operator typed. It is bound to the evidence and
  covered by the signature, but it is not authenticated.
- **Legal admissibility.** This is a tamper-evidence mechanism, not a certified process.
