# Capacity Planning Worksheet

**Service Name:** ___________________
**Date:** ___________________

## 1. Current Baseline
| Metric | Value | Source |
| :--- | :--- | :--- |
| **Peak RPS** (Requests/Sec) | | Prometheus |
| **Avg Latency** (Seconds) | | Prometheus |
| **CPU Usage** (Cores) | | Kubernetes |
| **Memory Usage** (GB) | | Kubernetes |

## 2. Growth Forecast
**Scenario:** (e.g., "Marketing Launch Q3")
**Expected Traffic Multiplier:** (e.g., 2.5x)

## 3. Calculation
**Projected RPS** = Peak RPS * Multiplier = ___________

**Estimated Cores Needed:**
(Projected RPS / Current RPS) * Current CPU Usage = ___________ Cores

**Headroom Buffer (+30%):**
Estimated Cores * 1.30 = **___________ Total Cores Required**

## 4. Action Plan
- [ ] Request quota increase (if needed).
- [ ] Update Kubernetes `replicas` or HPA settings.
