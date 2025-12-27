# Observability Demo: Golden Signals

This module provides a hands-on environment to visualize the **5 Golden Signals** (Latency, Traffic, Errors, Saturation) using Prometheus and Grafana.

## Contents
*   **`app/`**: Python web app that generates fake traffic metrics (including random errors and spikes).
*   **`docker-compose.yml`**: Full stack for local development.
*   **`k8s/`**: Kubernetes manifests for cluster deployment.

## Quick Start (Docker)
1.  Run the stack:
    ```bash
    docker-compose up -d
    ```
2.  Open Grafana at [http://localhost:3000](http://localhost:3000) (User: `admin`, Pass: `admin`).
3.  Add Data Source -> Prometheus -> URL: `http://prometheus:9090`.
4.  Explore metrics like `http_request_duration_seconds_count` (Traffic) or `http_request_errors_total` (Errors).

## Quick Start (Kubernetes)
1.  Deploy:
    ```bash
    kubectl apply -f k8s/
    ```
2.  Forward Grafana port:
    ```bash
    kubectl port-forward svc/grafana 3000:3000
    ```
3.  Access Grafana as above.

## The "Golden Signals" Implementation
*   **Latency:** `http_request_duration_seconds` (Histogram)
*   **Traffic:** `rate(http_request_duration_seconds_count[1m])`
*   **Errors:** `rate(http_request_errors_total[1m])`
*   **Saturation:** `app_queue_depth_items` (Gauge)
