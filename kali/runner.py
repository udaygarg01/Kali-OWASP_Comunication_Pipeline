import json
import subprocess
from pathlib import Path

JOB_FILE = Path("/scan/job.json")
OUTPUT_FILE = Path("/scan/result.json")

job = json.loads(JOB_FILE.read_text())
target = job["target"]

print(f"[KALI] Scanning target: {target}", flush=True)

subprocess.run(
    [
        "/usr/share/zaproxy/zap.sh",
        "-cmd",
        "-quickurl", target,
        "-quickout", str(OUTPUT_FILE)
    ],
    check=False
)

print("[KALI] Scan complete", flush=True)
