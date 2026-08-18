import subprocess
import tempfile
import os
import re
import sys


def extract_code(raw_response: str) -> str:
    match = re.search(r"```(?:python)?\n(.*?)```", raw_response, re.DOTALL)
    if match:
        return match.group(1)
    return raw_response


def run_test(generated_code: str, test_code: str, timeout: int = 5) -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        sol_path = os.path.join(tmpdir, "solution.py")
        test_path = os.path.join(tmpdir, "test_solution.py")

        with open(sol_path, "w") as f:
            f.write(generated_code)
        with open(test_path, "w") as f:
            f.write(test_code)

        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", test_path, "-q"],
                cwd=tmpdir,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            passed = result.returncode == 0
            output = result.stdout[-2000:] + result.stderr[-2000:]
            return {"passed": passed, "output": output, "timed_out": False}
        except subprocess.TimeoutExpired:
            return {"passed": False, "output": "timed out", "timed_out": True}
        except Exception as e:
            return {"passed": False, "output": str(e), "timed_out": False}