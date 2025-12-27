# Service Tiers & SLAs

This document defines the service tiers for our applications and the associated Service Level Agreements (SLAs) for incident response.

## Service Tiers

### Tier A: Critical (Platinum)
*   **Definition:** Services where downtime causes immediate and significant revenue loss or severe brand damage. These are the "Core Critical Path".
*   **Examples:** User Login, Checkout/Payments, Core API Gateway.
*   **Target Availability:** 99.9% - 99.99%

### Tier B: High (Gold)
*   **Definition:** Important services where downtime is painful but workarounds exist, or the impact is not immediately critical to the bottom line.
*   **Examples:** Search, User Profiles, Recommendation Engine, Reporting (deferred).
*   **Target Availability:** 99.0% - 99.9%

### Tier C: Standard (Silver)
*   **Definition:** Internal tools, non-critical features, experimental changes.
*   **Examples:** Admin Dashboard, Beta features, Internal Wiki.
*   **Target Availability:** 95.0% - 99.0%

---

## Incident Management SLAs

| Metric | Tier A (Critical) | Tier B (High) | Tier C (Standard) |
| :--- | :--- | :--- | :--- |
| **Response Time (TTA)** | **< 15 mins** (24/7) | **< 1 hour** (24/7*) | **< 8 hours** (Biz Hours) |
| **Resolution Time (TTR)**| **< 4 hours** | **< 24 hours** | **Best Effort / 5 days** |

*\*Note: Tier B 24/7 coverage depends on specific team agreements. Default is Extended Business Hours.*

### Definitions
*   **TTA (Time To Acknowledge):** Time from alert firing to human acknowledgement.
*   **TTR (Time To Resolve):** Time from alert firing to service restoration (mitigation).
