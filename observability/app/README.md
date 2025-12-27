# Golden Signals Application

A simulation app designed to generate interesting metrics for observability demos.

## Features
*   Generates **HTTP Metrics** (Latency, Count).
*   Simulates **Errors** (Random HTTP 500s).
*   Simulates **Latency Spikes** (Random sleeps).
*   Simulates **Saturation** (Random queue depth gauge).

## Usage
*   **Docker:** Built automatically via `docker-compose up` in the parent directory.
*   **Manual:** `python app.py` (Requires `flask`, `prometheus_client`).
*   **Endpoint:** Metrics are exposed at `/metrics`.
