# Postmortem Template

**Date:** YYYY-MM-DD
**Authors:**
**Status:** [Draft | Review | Complete]
**Severity:** [SEV-1 | SEV-2 ...]
**Impact:** (e.g., "5% of users got 500 errors on checkout for 20 mins")
**Root Cause:** (Brief summary)

## Executive Summary
*One paragraph summary for leadership. What happened, why, and how did we fix it?*

## Timeline
*(All times in UTC)*
*   **HH:MM** - Alert fired for high latency.
*   **HH:MM** - Engineer A acknowledged alert.
*   **HH:MM** - Incident declared.
*   **HH:MM** - Rollback started.
*   **HH:MM** - Incident resolved.

## Root Cause Analysis (5 Whys)
1.  **Why did the checkout fail?** Database connection timeout.
2.  **Why did the DB timeout?** Connection pool was exhausted.
3.  **Why was the pool exhausted?** New feature X introduced a query without a limit.
4.  **Why did the query lack a limit?** Reviewer missed the missing pagination.
5.  **Why did we miss it?** No linting rule for unpaginated queries.

## Lessons Learned
### What went well?
*   Alerts fired instantly.
*   Rollback was fast (2 mins).

### What went wrong?
*   Canary environment didn't catch the load issue.
*   Runbook for DB restart was outdated.

## Action Items
| ID | Task | Owner | Priority | Ticket |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Add linting for SQL pagination | @dev-lead | P1 | TICKET-123 |
| 2 | Update Load Testing to simulate feature X | @qa-lead | P2 | TICKET-124 |
