# How to Create a GitHub App for Harness

To enable the best integration (GitOps, PR status checks, Triggers), use a **GitHub App**.

## 1. Create the App in GitHub
1.  Go to **Settings** > **Developer settings** > **GitHub Apps** > **New GitHub App**.
2.  **GitHub App Name**: `Harness-SRE-Roadmap-Integration` (must be unique).
3.  **Homepage URL**: `https://app.harness.io`
4.  **Callback URL**: `https://app.harness.io/auth/github/callback`
5.  **Webhook**: Uncheck "Active" (unless you specifically need it for triggers now, Harness usually handles this via the creating flow or you can add it later).

## 2. Set Permissions
These are the recommended permissions for a CI/CD Pipeline:

*   **Repository permissions:**
    *   **Checks:** Read & write (To report pipeline status on PRs).
    *   **Contents:** Read & write (To clone code and push changes/tags).
    *   **Metadata:** Read-only (Required).
    *   **Pull Requests:** Read & write (To comment on PRs).
    *   **Webhooks:** Read & write.

*   **Subscribe to events:**
    *   Check **Pull request**.
    *   Check **Push**.

## 3. Generate Credentials
1.  Click **Create GitHub App**.
2.  **App ID**: Copy this number.
3.  **Client ID**: Copy this string.
4.  **Client Secret**: Click "Generate a new client secret" and copy it.
5.  **Private Key**: Click "Generate a private key". It will download a `.pem` file.

## 4. Install the App
1.  On the left sidebar, click **Install App**.
2.  Click **Install** next to your account (`aacshar14`).
3.  Select **Only select repositories** -> `SRE-roadmap`.
4.  Click **Install**.

## 5. Configure in Harness
1.  Go to **Connectors** -> **New Connector** -> **GitHub**.
2.  **Overview**: Name it `GitHub_App_SRE`.
3.  **Details**:
    *   **URL Type**: Account (`https://github.com/aacshar14`)
    *   **Connection Type**: HTTP/HTTPS
    *   **Authentication**: **GitHub App**
    *   **App ID**: Paste from Step 3.
    *   **Installation ID**: You can find this in the URL of your installed app page (e.g. `github.com/settings/installations/12345678`), or Harness can try to fetch it.
    *   **Private Key**: Upload the `.pem` file content as a **Harness File Secret**.
