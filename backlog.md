# SRE Platform Refinement Backlog

This document lists items identified for future refinement to improve the usability and robustness of the platform.

## 🏃 Quick Wins (Usability)
- [ ] **Create `.env.example`:** The Golden Signals app uses some hardcoded defaults. We should abstract them to a `.env` file.
- [ ] **Add `Makefile`:** Create a `makefile` with shortcuts like `make build`, `make chaos`, `make deploy`.
- [ ] **Pre-commit Hooks:** Add `pre-commit` to lint Python and Terraform code automatically before pushing.

## 🔧 Technical Debt (Refactoring)
- [ ] **Chaos Config Externalization:** Currently, chaos state is in-memory. If the app restarts (pod killed), chaos settings are lost. Consider moving chaos state to Redis or a ConfigMap hot-reload.
- [ ] **Terraform State Management:** Move `terraform.tfstate` from local disk to a remote backend (Azure Blob Storage / S3) to support team collaboration.

## 🔒 Security
- [ ] **Secrets Management:** Integrate Harness Secrets or Vault instead of using local vars for credentials.
- [ ] **Image Scanning:** Add a step in the Harness Pipeline to scan Docker images for vulnerabilities (Trivy/Snyk).

## 📊 Observability
- [ ] **SLO Dashboard:** standard Grafana dashboard specifically for tracking Error Budget Burn Rate.
