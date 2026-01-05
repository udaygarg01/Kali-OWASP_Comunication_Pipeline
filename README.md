
# Kali OWASP Communication Pipeline (POC)

## Overview

This repository contains a **Proof of Concept (POC)** implementation for executing OWASP ZAP scans using **ephemeral Kali Linux containers**, orchestrated via Python.

The goal of this POC is to demonstrate:

* Safe execution of security scanning tools from Kali Linux
* One-job-one-container execution model
* No shared state between scans
* JSON-based input/output suitable for AI or automation pipelines
* Industry-standard orchestration pattern

This repository is **not a production system**. It is an architectural validation.

---

## Architecture Summary

* Each scan request launches a **new Kali container**
* The container executes OWASP ZAP using CLI mode
* Scan input is provided via `job.json`
* Scan output is produced as `result.json`
* The container exits immediately after completion

There is **no shared container**, **no docker exec**, and **no persistent runtime**.

---

## Repository Structure

```
.
├── orchestrator.py        # Worker / orchestrator logic
├── submit_job.py          # Entry point to submit a scan
├── kali/
│   ├── Dockerfile         # Kali-based scanner image
│   └── runner.py          # Tool execution logic (inside container)
└── jobs/
    └── README.md          # Runtime job directories are created here
```

---

## Prerequisites

Ensure the following are installed on your system:

* Docker (Docker Desktop is sufficient)
* Python 3.9 or later
* Git

No additional services (Redis, Kubernetes, etc.) are required for this POC.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/udaygarg01/Kali-OWASP_Comunication_Pipeline.git
cd Kali-OWASP_Comunication_Pipeline
```

---

### 2. Build the Kali Scanner Image

This builds the immutable Kali image used for all scans.

```bash
cd kali
docker build -t kali-scanner .
cd ..
```

Verify the image exists:

```bash
docker images | grep kali-scanner
```

---

### 3. Create and Activate Python Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
```

Activate:

* **Windows**

  ```bash
  .venv\Scripts\activate
  ```

* **Linux / macOS**

  ```bash
  source .venv/bin/activate
  ```

No external Python dependencies are required.

---

## Running the POC

### 4. Submit a Scan Job

Run the following command from the repository root:

```bash
python submit_job.py
```

By default, this submits a scan job for a placeholder test URL.

---

### 5. What Happens Internally

1. A unique job ID is generated
2. A job directory is created under `jobs/<job_id>/`
3. `job.json` is written with scan details
4. A new Kali container is launched
5. OWASP ZAP runs inside the container
6. Results are written to `result.json`
7. Container exits and is destroyed
8. Orchestrator reads and prints the result

---

## Output

After execution, you will see:

* Console logs showing job lifecycle
* A new directory under `jobs/`
* A `result.json` file containing scan output

Example:

```
jobs/
└── 9c2c6b7e-xxxx/
    ├── job.json
    └── result.json
```

The JSON output is machine-readable and suitable for further normalization or AI processing.

---

## Important Notes

* This POC uses **OWASP ZAP CLI mode (`zap.sh`)**, not baseline scripts
* Kali Linux does **not** ship `zap-baseline.py`
* All scans are executed in **isolated containers**
* No real production or client systems should be scanned


---

## Future Extensions (Out of Scope for POC)

* Redis / MQ integration
* Multiple concurrent workers
* Additional tools (Nmap, SQLmap, Nuclei)
* Unified vulnerability normalization
* AI-driven correlation and prioritization

---

## Conclusion

This POC validates a **production-safe execution pattern** for Kali-based security tooling:

* Ephemeral containers
* Strong isolation
* Deterministic execution
* Clean JSON outputs

