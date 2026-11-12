# ForensicTrace — deployment guide

Follow these steps in order on Linux x86_64. Tested on **Ubuntu 24.04.4** (kernel 7.0); other distributions such as Ubuntu 22.04 or Debian 12 should work but were not tested.

---

## Step 1 — Get the code

```bash
git clone https://github.com/D-Agbikossi/ForensicTrace_Capstone_Final.git
cd ForensicTrace_Capstone_Final/forensictrace
```

---

## Step 2 — Install tools (one time)

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev python3 curl
# for the experiment and statistics scripts (setup.sh installs these too):
sudo apt install -y python3-pandas python3-numpy python3-scipy valgrind
```

| Package | Why |
|---------|-----|
| `build-essential` | `gcc`, `make` |
| `libssl-dev` | SHA-256 sidecar |
| `python3` | Tests and `view_timeline.py` |
| `curl` | Scenario scripts |
| `python3-pandas`, `-numpy`, `-scipy` | `run_experiments.py` and `analyze.py` |

---

## Step 3 — Build and test

**Option A — automatic (recommended)**

```bash
bash scripts/setup.sh
```

You should see `Setup complete` and **127 tests passed**.

**Option B — manual**

```bash
make clean && make
chmod +x tests/run_tests.sh scenarios/*.sh scripts/*.sh
./tests/run_tests.sh
```

Build uses **`Makefile`** in this folder (`make`). There is no `make install`.

---

## Step 4 — Run your first trace

```bash
./forensictrace --config B --output /tmp/run.json -- /bin/ls /tmp
```

| Part | Meaning |
|------|---------|
| `--config B` | Process + **file** syscalls (use `A`, `C`, or `D` to change scope) |
| `--output /tmp/run.json` | Where to save the experiment |
| `--` | End of ForensicTrace options |
| `/bin/ls /tmp` | Command to trace |

You do **not** need `sudo` for normal runs.

**Output**

- **Terminal:** timeline table  
- **Files:** `/tmp/run.json`, `/tmp/run.json.sha256`, and the custody files `/tmp/run.json.manifest.json` and `/tmp/run.json.audit.jsonl` (see [custody.md](custody.md))

---

## Step 5 — Check integrity and read the timeline

```bash
sha256sum -c /tmp/run.json.sha256
python3 scripts/view_timeline.py /tmp/run.json
```

If verification prints `FAILED`, the JSON was changed after the run — capture again. To see which records changed, run `./forensictrace verify /tmp/run.json`.

Each JSON file includes `"truncated": true` if the run hit the 20,000-event cap (extra events were dropped).
Parent directories for `--output` are created automatically (e.g. `/tmp/my_run/out.json`).

---

## Step 6 — Run a lab scenario (optional)

```bash
./forensictrace --config B --output /tmp/scenario4.json -- bash scenarios/scenario04_file_corruption.sh
python3 scripts/view_timeline.py /tmp/scenario4.json
```

Other scripts: `scenarios/scenario01_download_execute.sh` (needs port **8765**), `scenario02_*`, `scenario03_*` (port **8766**).

---

## Step 7 — Run a demo (optional)

```bash
bash scripts/demo.sh
```

It builds, runs the tests and walks through tracing, integrity checking, custody verification and scenario 4.

---

## Step 8 — Use the dashboard (optional)

```bash
make keys        # once: signing key in ~/.config/forensictrace/
make dashboard   # then open http://127.0.0.1:8377
```

Select **New investigation** and run scenario 5. When it opens, the **Reports** page gives its technical and plain-language reports as PDF. See [dashboard.md](dashboard.md). Scenario 5 needs ports **8767** and **8768**; the dashboard itself uses **8377**.

---

## Step 9 — Put the dashboard online (optional)

There are two ways, and they do different things:

| | Render (public link) | GitHub Codespaces (full tool) |
|---|---|---|
| Who can open it | Anyone with the link | Only you, signed in to GitHub |
| New investigations | No: read-only demo | Yes, if the codespace allows tracing |
| Shows | Demo case, 128 study runs, comparison, custody, reports | Everything |
| Cost | Free web service; it sleeps when idle | Free monthly allowance for personal accounts |

Free tiers change, so check each platform's current terms before relying on them.

### Option A: public read-only demo on Render

Hosting platforms block `ptrace`, so the online copy shows recorded evidence and verifies it but cannot trace. `dashboard/server.py --public` listens on all interfaces, reads the port from `$PORT`, and refuses every request that would run, log or export anything.

1. Commit and push the repository to GitHub, including `forensictrace/Dockerfile` and `forensictrace/.dockerignore`.
2. Optional check on your laptop:
   ```bash
   cd forensictrace
   docker build -t forensictrace-demo .
   docker run --rm -e PORT=10000 -p 8390:10000 forensictrace-demo
   ```
   Open http://127.0.0.1:8390. You should see a "Read-only demo" notice.
3. Create a free account at https://render.com and sign in with GitHub.
4. Select **New** > **Web Service**, then connect the `ForensicTrace_Capstone_Final` repository.
5. Fill in:
   - **Root Directory:** `forensictrace`
   - **Runtime / Language:** Docker
   - **Instance type:** Free
   - **Health check path:** `/` (under Advanced, if shown)

   Leave the start command empty; the Dockerfile sets it.
6. Select **Create Web Service** and wait for the build log to show
   `ForensicTrace dashboard, read-only public demo, on port ...`.
7. Open the `https://<name>.onrender.com` address Render shows. A free service sleeps after a period without visits, so the first visit afterwards can take about a minute.

Every push to the branch redeploys it. Before sharing the link, remember that the evidence files contain your Linux user name, host name and file paths.

### Option B: the full tool in GitHub Codespaces

The repository's `.devcontainer/devcontainer.json` installs the build tools, builds the engine, runs the tests and asks for the `SYS_PTRACE` capability that tracing needs.

1. Commit and push the `.devcontainer` folder.
2. On the repository's GitHub page, select **Code** > **Codespaces** > **Create codespace on main**, and wait for setup to finish. It builds and runs `make test`, which takes a few minutes.
3. In the codespace terminal:
   ```bash
   cd forensictrace
   make keys
   make dashboard
   ```
   The server recognises the codespace and accepts its forwarded address.
4. Open the **Ports** tab, find port **8377** and open it in the browser. Keep its visibility **Private**: the full dashboard can start traces, so do not make the port public.
5. Stop the codespace when you finish, so it does not use your free hours.

If tracing fails with `Operation not permitted`, the codespace did not get the `SYS_PTRACE` capability. The read-only parts still work.

---

## Config quick reference

| Config | What is recorded |
|--------|------------------|
| **A** | Process only (`execve`, `fork`, `exit`, …) |
| **B** | A + files (`open`, `read`, `write`, `unlink`, …) |
| **C** | B + network (`connect`, …) |
| **D** | All syscalls |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `make` fails | Install `build-essential` and `libssl-dev` |
| **0 events** | Do not run under `strace`, `gdb`, or the IDE debugger |
| Tests fail on scenario 1 | Install `curl`; free port **8765** |
| `PTRACE_TRACEME: Operation not permitted` | Close other tracers; trace only via `./forensictrace -- …`. In a container, add `--cap-add=SYS_PTRACE` |
| Online dashboard says "forbidden host" | Start it with `--public` (read-only) or `--allow-host <address>` |

---

## Where files live

| Item | Location |
|------|----------|
| Binary (after build) | `./forensictrace` (not committed to Git) |
| Your traces | Any path you pass to `--output` (e.g. `/tmp/…`) |
| Investigations started from the dashboard | `cases/` (not committed to Git) |
| Exported evidence bundles | `exports/` (not committed to Git) |
| Your signing key | `~/.config/forensictrace/investigator.key` and `.pub` (never commit the `.key`) |
| Investigation reports | Dashboard **Reports** page, or `python3 scripts/case_report.py <evidence.json> --pdf <out.pdf>` |
| Study reports | `docs/technical_report.md`, `docs/report_for_general_readers.md`; PDFs rebuilt with `make reports` |
| Helper scripts | `scripts/setup.sh`, `scripts/demo.sh`, `scripts/view_timeline.py` |
