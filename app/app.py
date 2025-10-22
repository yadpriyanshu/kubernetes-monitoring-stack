from flask import Flask
from prometheus_client import Counter, generate_latest, REGISTRY
import time

app = Flask(__name__)

# Define metrics
requests_total = Counter('requests_total', 'Total number of requests')
request_latency_seconds = Counter('request_latency_seconds', 'Request latency in seconds')

@app.route('/')
def hello():
    start_time = time.time()
    requests_total.inc()
    time.sleep(0.1)  # Simulate work
    latency = time.time() - start_time
    request_latency_seconds.inc(latency)
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)