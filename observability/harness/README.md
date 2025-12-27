# Harness CI/CD

Configuration for automating the build and deployment via Harness.io.

## Files
*   **`pipeline.yaml`:** A declarative Pipeline definition.
    *   **Build Stage:** Builds Docker image from `../app/Dockerfile`.
    *   **Deploy Stage:** Deploys manifests from `../k8s/` to a Kubernetes cluster.

## Setup
*   **[Full Integration Guide (PAT & Troubleshooting)](./harness-github-integration.md):** Read this if you have connection errors.
*   **[GitHub App Guide (Advanced)](./github-app-setup.md):** For production-grade setup.

In Harness, use "Import from Git" and point to this file path:
`observability/harness/pipeline.yaml`
