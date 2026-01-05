import json
import subprocess
import uuid
from pathlib import Path

JOBS_DIR = Path("jobs").resolve()
JOBS_DIR.mkdir(exist_ok=True)

def run_scan(target_url: str):
    job_id = str(uuid.uuid4())
    job_dir = (JOBS_DIR / job_id).resolve()
    job_dir.mkdir(parents=True)

    job = {
        "job_id": job_id,
        "target": target_url
    }

    (job_dir / "job.json").write_text(json.dumps(job, indent=2))

    print(f"[ORCH] Launching scan job {job_id}")
    print(f"[ORCH] Job directory: {job_dir}")

    result = subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{job_dir}:/scan",
            "kali-scanner"
        ],
        text=True
    )

    result_file = job_dir / "result.json"

    if not result_file.exists():
        raise RuntimeError("Scan failed: result.json not produced")

    print(f"[ORCH] Scan finished for {job_id}")
    return json.loads(result_file.read_text())
