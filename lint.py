import os
import json
import subprocess

files = os.environ["INPUT_FILES"].split()

results = {}

for file in files:
    cmd = ["verilator", "--lint-only", file]

    process = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if process.returncode == 0:
        results[file] = "PASS"
    else:
        results[file] = "FAIL"

print(json.dumps(results, indent=2))

github_output = os.environ.get("GITHUB_OUTPUT")

if github_output:
    with open(github_output, "a") as f:
        f.write(f"result={json.dumps(results)}\n")
