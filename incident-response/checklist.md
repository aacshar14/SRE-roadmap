# Incident Commander (IC) Checklist

Use this checklist when leading a production incident response.

## Phase 1: Detection & Declaration
- [ ] **Confirm Severity:** Is this SEV-1, SEV-2, etc.? (See `severity-levels.md`)
- [ ] **Open Incident Channel:** Create a dedicated Slack/Teams channel (e.g., `#inc-123-login-down`).
- [ ] **Assign Roles:**
    -   **IC (Incident Commander):** You. Leader, coordinator, **not** the debugger.
    -   **Ops Lead:** The primary person debugging/fixing.
    -   **Comms Lead:** Updates stakeholders/users.
- [ ] **Start Log:** Pin a document or message to track timeline and updates.

## Phase 2: Investigation & Mitigation
- [ ] **Focus on Mitigation:** The goal is to stop the bleeding, not find the root cause yet.
    -   *Can we rollback?*
    -   *Can we drain traffic?*
    -   *Can we toggle a feature flag?*
- [ ] **Regular Updates:** Ask Ops Lead for status every 15-30 mins.
- [ ] **Delegate:** If Ops Lead is stuck, page more subject matter experts (SMEs).

## Phase 3: Resolution
- [ ] **Confirm Stability:** Monitoring shows recovery.
- [ ] **Verify User Impact:** Are users actually seeing success? (Check RUM).
- [ ] **Close Incident:** Declare "All Clear".

## Phase 4: Post-Incident
- [ ] **Save Artefacts:** Logs, graphs, chat history.
- [ ] **Schedule Postmortem:** Within 24-48 hours.
- [ ] **Update Ticket:** Ensure time-to-detect and time-to-resolve are recorded.
