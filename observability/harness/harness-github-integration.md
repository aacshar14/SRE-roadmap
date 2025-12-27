# Connect Harness.io to GitHub

This guide explains how to set up the **Git Connector** in Harness to import pipelines and enable GitOps.

## Option 1: Personal Access Token (PAT) - Quickest
Use this for personal testing or simple setups.

### 1. Generate Token in GitHub
1.  Go to **Settings** > **Developer Settings** > **Personal access tokens** > **Tokens (classic)**.
2.  Click **Generate new token (classic)**.
3.  **Scopes:** Select `repo` (Full control of private repositories) and `read:org` (if needed).
4.  Copy the generated token (begins with `ghp_...`).

### 2. Create Connector in Harness
1.  Go to **Project Setup** > **Connectors** > **New Connector** > **GitHub**.
2.  **Overview:** Name it `GitHub_PAT`.
3.  **Details:**
    *   **URL Type:** `Account`.
    *   **Harness Account URL:** `https://github.com/aacshar14`
    *   **Connection Type:** `HTTP/HTTPS`.
4.  **Credentials:**
    *   **Username:** `aacshar14`
    *   **Personal Access Token:** Create a generic secret with the token you copied.
    *   **Enable API Access:** **IMPORTANT:** Make sure this is enabled/checked if available, or implied by providing the token.
5.  Click **Save & Test**.

---

## Option 2: GitHub App - Recommended for SRE/Ops
Use this for production, proper PR status checks, and avoiding rate limits.

*   See the detailed [GitHub App Setup Guide](./github-app-setup.md).

---

## Troubleshooting Common Errors

### "Invalid request: The given connector..." or "YAML path is required"
This usually happens during the "Import from Git" wizard if the connector cannot list the repository contents via API.

**Fix:**
1.  Ensure you are using a **Connector** with **API Access** enabled (Username + Token, NOT Anonymous).
2.  **Repository Name:** Try entering just the short name `SRE-roadmap` instead of the full URL, or vice versa, depending on how you configured the connector URL.
    *   If Connector URL is `https://github.com/aacshar14` -> Repository: `SRE-roadmap`
    *   If Connector URL is `https://github.com/aacshar14/SRE-roadmap.git` -> Repository: (Leave empty or try `SRE-roadmap`)
3.  **YAML Path:** Must be the relative path from root: `observability/harness/pipeline.yaml`

### "RepoName does not match"
Your connector is pointing to a specific repo (e.g. `SRE-roadmap`), but you provided a full URL in the pipeline wizard.
*   **Fix:** Use an Account-level connector (`https://github.com/aacshar14`) so you can type the repo name freely.
