import os
import json
import time
import requests
from dotenv import load_dotenv

from tasks import TASKS
from score import extract_code, run_test

load_dotenv()

RUNS_PER_TASK = 3
RESULTS_PATH = "results.jsonl"

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

MODELS = {
    "gemini-3.5-flash": {
        "model_id": "gemini-3.5-flash",
    },
    "gemini-3.5-flash-lite": {
        "model_id": "gemini-3.5-flash-lite",
    },
}

SYSTEM_PROMPT = (
    "You are a Python coding assistant. Given a function spec, output ONLY the "
    "function implementation in a single python code block. No explanation, no "
    "extra text, no example usage outside the function."
)


def call_gemini(model_key: str, prompt: str) -> dict:
    model_id = MODELS[model_key]["model_id"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent"

    start = time.time()
    resp = requests.post(
        url,
        headers={
            "x-goog-api-key": GEMINI_API_KEY,
            "Content-Type": "application/json",
        },
        json={
            "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        },
        timeout=60,
    )
    latency = time.time() - start
    data = resp.json()

    if "candidates" not in data:
        raise RuntimeError(f"Gemini API error: {data}")

    text = "".join(p.get("text", "") for p in data["candidates"][0]["content"]["parts"])
    usage = data.get("usageMetadata", {})
    return {
        "text": text,
        "input_tokens": usage.get("promptTokenCount", 0),
        "output_tokens": usage.get("candidatesTokenCount", 0),
        "latency": latency,
    }


def run_task(task: dict, model_key: str, run_number: int) -> dict:
    response = call_gemini(model_key, task["prompt"])
    code = extract_code(response["text"])
    test_result = run_test(code, task["test_code"])

    return {
        "task_id": task["id"],
        "difficulty": task["difficulty"],
        "model": model_key,
        "run": run_number,
        "passed": test_result["passed"],
        "timed_out": test_result["timed_out"],
        "input_tokens": response["input_tokens"],
        "output_tokens": response["output_tokens"],
        "cost": 0.0,
        "latency": response["latency"],
        "generated_code": code,
        "test_output": test_result["output"][-500:],
    }


def main():
    if not GEMINI_API_KEY:
        raise SystemExit("Set GEMINI_API_KEY")

    completed = set()
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            for line in f:
                r = json.loads(line)
                completed.add((r["task_id"], r["model"], r["run"]))

    with open(RESULTS_PATH, "a") as out:
        for task in TASKS:
            for model_key in MODELS:
                for run_number in range(1, RUNS_PER_TASK + 1):
                    key = (task["id"], model_key, run_number)
                    if key in completed:
                        continue
                    print(f"task {task['id']} | {model_key} | run {run_number}")
                    try:
                        result = run_task(task, model_key, run_number)
                    except Exception as e:
                        result = {
                            "task_id": task["id"], "difficulty": task["difficulty"],
                            "model": model_key, "run": run_number, "passed": False,
                            "timed_out": False, "error": str(e),
                        }
                    out.write(json.dumps(result) + "\n")
                    out.flush()
                    time.sleep(2)


if __name__ == "__main__":
    main()