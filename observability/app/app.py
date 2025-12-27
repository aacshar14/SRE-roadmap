import time
import random
from flask import Flask, Response, request
from prometheus_client import generate_latest, Counter, Histogram, Gauge

app = Flask(__name__)

# --- Metrics ---
# 1. LATENCY (and Traffic via count)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

# 2. ERRORS
REQUEST_ERRORS = Counter(
    'http_request_errors_total',
    'Total number of 500 errors',
    ['method', 'endpoint']
)

# 3. SATURATION (Simulated Queue Depth)
QUEUE_DEPTH = Gauge(
    'app_queue_depth_items',
    'Current items in the processing queue'
)

# --- Routes ---

@app.route('/')
def home():
    # Simulate processing time
    sleep_time = random.uniform(0.01, 0.2)
    
    # Randomly spike latency (1 in 20 requests)
    if random.random() < 0.05:
        sleep_time += 1.5 
    
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        time.sleep(sleep_time)
        
        # Simulate Saturation fluctuation
        QUEUE_DEPTH.set(random.randint(5, 50))
        
        # Simulate Random 500 Errors
        if random.random() < 0.1: # 10% error rate
            REQUEST_ERRORS.labels(method='GET', endpoint='/').inc()
            return Response("Internal Server Error", status=500)
            
    return "Hello Golden Signals!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
