# Severity Levels

Defining severity helps set clear expectations for response times and stakeholder communication.

| Level | Description | Example | Response SLA |
| :--- | :--- | :--- | :--- |
| **SEV-1 (Critical)** | **System Down / Large Impact.** Critical business function unavailable for >10% of users. Data loss risk. | Login down. Checkout failing. Security breach. | **Immediate (24/7)**. Wake up everyone needed. |
| **SEV-2 (High)** | **Major Feature Broken.** Workarounds exist but are painful. Performance severely degraded. | Search is slow/unavailable. Report generation failing. | **Urgent (24/7)**. Page on-call immediately. |
| **SEV-3 (Moderate)** | **Minor User Impact.** Non-critical feature broken. Internal tools issues. | User profile avatar upload failing. Admin dashboard slow. | **Business Hours**. Handle next working day if off-hours. |
| **SEV-4 (Low)** | **Cosmetic / Trivial.** Minor bugs, typos, glitches. | CSS alignment issue. Typos in help text. | **SLA:** Standard ticket backlog. |
