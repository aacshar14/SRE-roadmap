# Kubernetes Manifests

Standard K8s manifests to deploy the Observability Demo stack.

## Contents
*   **`app.yaml`:** Deployment and Service for the Golden Signals App.
*   **`prometheus.yaml`:** Deployment, Service, and ConfigMap for Prometheus (configured for Kubernetes Service Discovery).
*   **`grafana.yaml`:** Deployment and Service (NodePort) for Grafana.

## Usage
```bash
kubectl apply -f .
```
Access Grafana via `kubectl port-forward svc/grafana 3000:3000`.
