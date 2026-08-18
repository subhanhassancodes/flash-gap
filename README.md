# ⚡ Flash Gap

**Does paying for Gemini's full Flash tier actually get you better code than the free,
low-latency Flash-Lite tier — or is the gap smaller than the pricing page implies?**

A 30-task, hand-verified, automatically-scored benchmark comparing **Gemini 3.6 Flash** ⚡
against **Gemini 3.5 Flash-Lite** ⚡ on self-contained Python coding correctness. Every
task is scored by actually *running* the generated code against hidden tests — no LLM
judge, no subjective grading, no cherry-picked examples.

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![Tasks](https://img.shields.io/badge/task%20suites-30%2F30%20verified-brightgreen)
![Cost](https://img.shields.io/badge/API%20cost-%240.00-success)

---

## 🎯 Why this exists

Almost every "model A vs. model B" claim online is an opinion with no task set behind it.
This benchmark exists to settle one specific, narrow question with real numbers instead
of vibes — and to publish everything (tasks, scoring code, raw results) so anyone can
rerun it and get the same answer.

**✅ What this measures:** single-shot, self-contained Python function generation, scored
by automated test execution, run 3x per model to separate real signal from sampling noise.

**🚫 What this explicitly does NOT measure:** multi-file or repo-level work, agentic /
tool-use ability, code style or readability, non-Python languages, or behavior across
different reasoning-effort settings. See [`tasks.py`](tasks.py) for the full task set.

---

## 🏗️ How it works

```
┌──────────────────────────────────┐
│ tasks.py                         │
│ 30 hand-verified problems        │
│ + hidden pytest suites           │
└──────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│ runner.py                        │
│ sends every task to:             │
│   - Gemini 3.6 Flash             │
│   - Gemini 3.5 Flash-Lite        │
│ 3 runs per model                 │
└──────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│ score.py                         │
│ sandboxed pytest execution       │
│ pass / fail / timeout            │
└──────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│ results.jsonl                    │
│ raw per-call data                │
└──────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│ analyze.py                       │
│ aggregates + writes report       │
└──────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────┐
│ results.md                       │
│ pass rate * variance * cost      │
│ * disagreements                  │
└──────────────────────────────────┘
```

| Step | File | What it does |
|---|---|---|
| 1️⃣ | [`tasks.py`](tasks.py) | 30 Python problems (⅓ easy / medium / hard), each with a hidden `pytest` suite |
| 2️⃣ | [`runner.py`](runner.py) | Sends every task to both models, 3 runs each (180 calls total) |
| 3️⃣ | [`score.py`](score.py) | Runs the generated function against its hidden tests in an isolated, timed subprocess |
| 4️⃣ | [`analyze.py`](analyze.py) | Aggregates everything into `results.md` — pass rate, variance, cost, disagreements |

Every one of the 30 test suites was verified bug-free against a correct reference
implementation ([`_reference_check/solution.py`](_reference_check/solution.py)) **before**
any model ever saw them.

---

## 📂 Repo structure

```
flash-gap/
├── tasks.py                    30 tasks + hidden test suites
├── score.py                    sandboxed test execution
├── runner.py                   calls both models, logs results
├── analyze.py                  builds results.md from raw data
├── _reference_check/
│   └── solution.py             correct reference impl, used to verify tasks.py
├── results.jsonl               raw per-call data (generated after running)
├── results.md                  final report (generated after running)
└── README.md
```

---

## ⚙️ Setup

```bash
pip install requests pytest
export GEMINI_API_KEY=your_key_here      # Windows: set GEMINI_API_KEY=your_key_here
```

Get a free key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey) — 🆓 no
credit card or billing account required for Flash / Flash-Lite on the free tier.

## ▶️ Running it

```bash
python3 runner.py      # 30 tasks x 2 models x 3 runs = 180 calls, ~6 minutes
python3 analyze.py     # writes results.md
```

`runner.py` is **resumable** 🔁 — if it's interrupted, rerunning it skips any
(task, model, run) combination already recorded in `results.jsonl`.

---

## 📊 Results

> *Run `python3 analyze.py` and paste the contents of the generated `results.md` here
> before publishing — pass rate by run and by difficulty, total cost, mean latency, and
> the disagreement list.*

**Before publishing:** open the disagreement list, look at the actual generated code for
a few of those tasks (saved per-call in `results.jsonl`), and write a short explanation of
*why* one model succeeded where the other failed. That's what turns this from a script
output into an actual finding. 🔍

---

## 🔬 Methodology notes

- **No partial credit.** A task passes only if 100% of its hidden tests pass — avoids
  subjective judgment calls about "almost correct."
- **3 runs per task per model**, reported as mean and standard deviation — a single run
  can't distinguish a real capability gap from ordinary sampling variance.
- **Tests verified before scoring anything real.** Every one of the 30 test suites was
  run against a known-correct reference implementation first, to rule out the benchmark
  itself being the buggy part.

---

## 👤 Author

**Syed Subhan Hassan**
[@subhanhassancodes](https://github.com/subhanhassancodes)
