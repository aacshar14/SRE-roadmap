# SRE Platform Onboarding Checklist

Welcome! If you are new to the team or onboarding a new project, follow this checklist to ensure you are compliant with our SRE standards.

## 1. Prerequisites
Before you start, ensure you have the following installed:
- [ ] **Git** (for version control)
- [ ] **Python 3.9+** (for scripts and app)
- [ ] **Docker** (for local testing)
- [ ] **Terraform** (for infrastructure)
- [ ] **Harness CLI** (optional, for CI/CD)

## 2. Platform Setup
- [ ] **Clone the Repo:** `git clone <repo-url>`
- [ ] **Install Dependencies:**
    ```bash
    pip install -r observability/app/requirements.txt
    ```

## 3. Register Your Service (Critical)
We use a centralized metadata repository. You **must** register your service to integrate with our automation.
- [ ] **Run the Registration Script:**
    ```bash
    python scripts/generate_postmortem.py --add-service
    ```
    *   *Input your Service Name, Team, and SLA Tier (A/B/C).*

## 4. Development Standards (12-Factor)
- [ ] **Config:** Ensure your app reads config from **Environment Variables**, not files.
- [ ] **Logs:** Ensure your app logs to `stdout/stderr` (no local log files).
- [ ] **Health Checks:** Implement `/health` and `/metrics` (Prometheus) endpoints.

## 5. Operations
- [ ] **Capacity Planning:** Fill out the [Worksheet](../capacity/worksheet.md) *before* deployment.
- [ ] **CI/CD:** Import the [Harness Pipeline](../observability/harness/pipeline.yaml).
- [ ] **Incidents:** Bookmark the [Incident Checklist](../incident-response/IC-checklist.md).
