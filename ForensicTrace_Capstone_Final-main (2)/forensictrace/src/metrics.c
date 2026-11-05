/*
 * metrics.c — CPU and memory measurement for one monitored run.
 *
 * RUSAGE_SELF      = ForensicTrace itself (the monitoring cost).
 * RUSAGE_CHILDREN  = the traced process tree that the tracer waited for
 *                    (the workload). Comparing the workload against an
 *                    unmonitored run of the same scenario gives the overhead
 *                    defined in the proposal (Table 5); scripts/run_experiments.py
 *                    performs that comparison.
 *
 * Storage volume is the final size of the JSON file (ft_write_json) and
 * processing time is measured per pipeline stage in main.c.
 */
#include "forensictrace.h"

#include <sys/resource.h>
#include <sys/time.h>

static uint64_t tv_us(struct timeval tv)
{
    return (uint64_t)tv.tv_sec * 1000000ULL + (uint64_t)tv.tv_usec;
}

void ft_resources_capture(FTContext *c)
{
    struct rusage self;
    struct rusage children;

    if (!c) {
        return;
    }
    getrusage(RUSAGE_SELF, &self);
    getrusage(RUSAGE_CHILDREN, &children);

    c->res.wall_ns = (c->end_ns > c->start_ns) ? (c->end_ns - c->start_ns) : 0;
    c->res.tracer_user_us = tv_us(self.ru_utime);
    c->res.tracer_sys_us = tv_us(self.ru_stime);
    c->res.workload_user_us = tv_us(children.ru_utime);
    c->res.workload_sys_us = tv_us(children.ru_stime);
    c->res.tracer_maxrss_kb = self.ru_maxrss;       /* KiB on Linux */
    c->res.workload_maxrss_kb = children.ru_maxrss;
}
