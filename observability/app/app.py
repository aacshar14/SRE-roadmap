import time
import random
import sys
import threading
from flask import Flask, Response, request, jsonify
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

# --- Chaos State ---
chaos_config = {
    "latency": False, # If True, add 2s delay
    "error": False    # If True, return 500
}

# --- Routes ---

@app.route('/')
def home():
    # Chaos: Latency Injection
    sleep_time = random.uniform(0.01, 0.2)
    if chaos_config["latency"]:
        sleep_time += 2.0
    # Randomly spike latency (1 in 20 requests) even without chaos
    elif random.random() < 0.05:
        sleep_time += 1.5 
    
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        time.sleep(sleep_time)
        
        # Simulate Saturation fluctuation
        QUEUE_DEPTH.set(random.randint(5, 50))
        
        # Chaos: Error Injection
        if chaos_config["error"] or (random.random() < 0.1): # 10% natural error rate
            REQUEST_ERRORS.labels(method='GET', endpoint='/').inc()
            return Response("Internal Server Error (Chaos or Random)", status=500)
            
    return "Hello Golden Signals! (Chaos: {})".format(chaos_config)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

# --- Chaos API ---
@app.route('/chaos/<mode>', methods=['POST'])
def chaos_toggle(mode):
    """
    /chaos/latency -> Toggle latency
    /chaos/error   -> Toggle errors
    /chaos/kill    -> Kill process
    """
    if mode == 'kill':
        def kill_me():
            time.sleep(1)
            sys.exit(1)
        threading.Thread(target=kill_me).start()
        return "Creating kernel panic... Goodbye!", 200
        
    if mode in chaos_config:
        chaos_config[mode] = not chaos_config[mode]
        return jsonify({"status": "updated", "config": chaos_config})
    
    return "Unknown mode", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
