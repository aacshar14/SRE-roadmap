# Chaos Engineering Experiments

This module allows you to stress test the Golden Signals application and observe how the system (and your dashboards) react to failure.

## 1. Prerequisites
*   The stack must be running (`docker-compose up` or deployed to K8s).
*   Port 5000 must be accessible.

## 2. Tools
*   **`stress.py`:** A Python script that acts as both a load generator and a Chaos Controller.

## 3. Playbook (Experiments)

### Experiment A: Latency Spike
*   **Goal:** Verify Prometheus "Latency" alert or dashboard spike.
*   **Action:**
    1.  Run `python stress.py`.
    2.  Select Option **1** (Toggle High Latency).
    3.  **Expectation:** Dashboard `http_request_duration_seconds` should jump to >2s.

### Experiment B: Error Storm
*   **Goal:** Verify SLO burn rate or Error Rate alert.
*   **Action:**
    1.  Select Option **2** (Toggle Error Mode).
    2.  **Expectation:** App counting 100% 500 status codes.

### Experiment C: The Kill (Self-Healing)
*   **Goal:** Verify Kubernetes (or Docker Restart policy) brings the app back.
*   **Action:**
    1.  Select Option **3** (Kill App).
    2.  **Expectation:**
        *   App crashes (connection refused momentarily).
        *   Kubernetes detects CrashLoop/Failure.
        *   Kubernetes restarts the Pod.
        *   Traffic resumes automatically after a few seconds.
