# SRE Workshop: Fundamentals and Practice

This workshop is designed to introduce you to the key concepts of Site Reliability Engineering (SRE), with a special focus on measuring reliability through SLIs and SLOs.

## Part 1: The 5 Golden Signals

For effective observability, Google recommends focusing on these key signals. We have added "Availability" as the fifth essential signal.

1.  **Latency:** The time it takes to serve a request.
    *   *Important:* Distinguish between success and error latency. A 500 error response might be very fast, skewing your metrics.
2.  **Traffic:** The demand placed on your system.
    *   *Example:* HTTP requests per second, or database transactions.
3.  **Errors:** The rate of requests that fail.
    *   *Types:* Explicit (HTTP 500), implicit (HTTP 200 but with empty or wrong content), or by policy (response > 1 sec).
4.  **Saturation:** How "full" your service is.
    *   *Metric:* CPU, memory, I/O usage. Measures the "busy" fraction of your most constrained resource.
5.  **Availability:** The percentage of time the system is usable.
    *   *Relation:* Often defined as a function of success rates from the other signals.

---

## Part 2: The 10 Fundamental Steps of SRE

1.  **Foundations & Culture:** SRE is not just technology. It relies on a "blameless" culture and psychological safety to report incidents.
2.  **SLIs (Service Level Indicators):** What precise metric tell us if the user is happy? (e.g., latency of 99% of requests).
3.  **SLOs (Service Level Objectives):** The numerical target for that SLI (e.g., 99.9% of requests must be successful).
4.  **Error Budgets:** 100% - SLO. This is the margin we have for failure. If depleted, releases are frozen to stabilize.
5.  **Toil Reduction:** Automating manual, repetitive tasks with no strategic value that scale linearly with the service.
6.  **Monitoring & Observability:** Implementing the 5 Golden Signals. Moving from "is the server up?" to "does the service work for the user?".
7.  **Incident Response:** Having clear roles (Incident Commander, Comms, Ops) and defined procedures before the fire starts.
8.  **Postmortems:** Detailed analysis after an incident. The goal is not to find culprits, but to fix the process or system that allowed the failure.
9.  **Capacity Planning:** Predicting future growth (organic or launch-driven) to ensure sufficient resources before saturation.
10. **Chaos Engineering & Resilience:** Breaking things on purpose in controlled environments to train the team and validate recovery systems.

---

## Part 3: Deep Dive - SLOs & SLIs

The core of SRE is data-driven decision making, and for that, we need to define what "reliability" means.

### Definitions

*   **SLI (Indicator):** A quantitative measure of some aspect of the level of service.
    *   `SLI = (Good Events / Total Events) * 100`
*   **SLO (Objective):** A target value or range of values for a service level that is measured by an SLI.
    *   `SLI >= SLO`

### Practical Example: Login Service

Imagine an authentication service.

**Step 1: Choose the SLI**
We don't care if CPU is at 10% or 90% if the user logs in fast.
*   *Metric:* Availability (Latency + Correctness).
*   *Definition:* The proportion of valid requests to `/login` that respond with HTTP 200 and in less than 500ms.

**Step 2: Define the SLO**
Do we need 100%? Probably not, and it's very expensive.
*   *Target:* 99.9% monthly.

**Step 3: Calculate the Error Budget**
In a 30-day window (approx 43,200 minutes), 99.9% availability means:
*   **Allowed Downtime:** 43.2 minutes (`43,200 * (1 - 0.999)`).

### Workshop Exercise

*Scenario:* You receive 1,000,000 requests per week. Your SLO is 99.95%.

1.  **How many requests can fail?**
    *   Total: 1,000,000
    *   Allowed to fail: 0.05% -> `0.0005 * 1,000,000` = **500 requests**.

2.  **Situation:** A Tuesday deploy caused 200 HTTP 500 errors over 5 minutes.
    *   Budget Consumption: 200 / 500 = 40%.
    *   *Decision:* You still have 60% of the budget. You can keep releasing features, but with caution.
