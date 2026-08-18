import json
from collections import defaultdict
from statistics import mean, stdev

from tasks import TASKS

DIFFICULTY = {t["id"]: t["difficulty"] for t in TASKS}


def load_results(path="results.jsonl"):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def pass_rate_by_run(rows, model):
    by_run = defaultdict(list)
    for r in rows:
        if r["model"] == model:
            by_run[r["run"]].append(1 if r.get("passed") else 0)
    return {run: mean(vals) for run, vals in sorted(by_run.items())}


def pass_rate_by_difficulty(rows, model):
    by_diff = defaultdict(list)
    for r in rows:
        if r["model"] == model:
            by_diff[r["difficulty"]].append(1 if r.get("passed") else 0)
    return {d: mean(vals) for d, vals in by_diff.items()}


def totals(rows, model):
    subset = [r for r in rows if r["model"] == model]
    cost = sum(r.get("cost", 0) for r in subset)
    latencies = [r["latency"] for r in subset if "latency" in r]
    return cost, mean(latencies) if latencies else 0


def disagreements(rows):
    by_task = defaultdict(dict)
    for r in rows:
        by_task[r["task_id"]].setdefault(r["model"], []).append(1 if r.get("passed") else 0)

    out = []
    for task_id, models in by_task.items():
        rates = {m: mean(v) for m, v in models.items()}
        if len(rates) == 2:
            vals = list(rates.values())
            if abs(vals[0] - vals[1]) >= 0.5:
                out.append((task_id, rates))
    return sorted(out, key=lambda x: -abs(list(x[1].values())[0] - list(x[1].values())[1]))


def main():
    rows = load_results()
    models = sorted(set(r["model"] for r in rows))

    lines = ["# Results\n"]

    for model in models:
        lines.append(f"## {model}\n")

        by_run = pass_rate_by_run(rows, model)
        run_vals = list(by_run.values())
        lines.append("**Pass rate by run:** " + ", ".join(f"run {k}: {v:.1%}" for k, v in by_run.items()))
        if len(run_vals) > 1:
            lines.append(f"**Mean: {mean(run_vals):.1%}, stdev: {stdev(run_vals):.1%}**\n")
        else:
            lines.append("")

        by_diff = pass_rate_by_difficulty(rows, model)
        lines.append("**Pass rate by difficulty:**")
        for d in ["easy", "medium", "hard"]:
            if d in by_diff:
                lines.append(f"- {d}: {by_diff[d]:.1%}")
        lines.append("")

        cost, avg_latency = totals(rows, model)
        lines.append(f"**Total cost (all runs):** ${cost:.4f}")
        lines.append(f"**Mean latency per call:** {avg_latency:.2f}s\n")

    lines.append("## Tasks where the two models disagreed most\n")
    lines.append("(pass rate gap >= 0.5 between models — start the failure/unfairness section here)\n")
    for task_id, rates in disagreements(rows):
        lines.append(f"- Task {task_id} ({DIFFICULTY.get(task_id, '?')}): " +
                      ", ".join(f"{m}={r:.0%}" for m, r in rates.items()))

    with open("results.md", "w") as f:
        f.write("\n".join(lines))

    print("wrote results.md")


if __name__ == "__main__":
    main()
