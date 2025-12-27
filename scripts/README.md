# SRE Automation Scripts

Helper scripts to automate SRE tasks.

## Scripts
*   **`generate_postmortem.py`:** A Python script to auto-create a Postmortem file.
    *   **Usage:** `python generate_postmortem.py`
    *   **Config:** Reads from `../incident-response/config/metadata.json`
    *   **Inputs:** Prompts for Title, Severity, and Authors.
    *   **Output:** Creates a new .md file in `../incident-response/postmortems/`
