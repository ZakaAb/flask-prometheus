from prometheus_client import Counter, start_http_server, Gauge
from flask import Flask

REQUESTS = Counter('http_requests_total', 'Total number of requests', labelnames=['path', 'method'])
ERRORS = Counter('http_errors_total', 'Total number of errors', labelnames=['code'])
IN_PROGRESS = Gauge('inprogress_requests', 'Total number of requests in progress')


"""
Question 13: PLACEHOLDER-1
"""

def before_request():
    IN_PROGRESS.inc()

def after_request(response):
    IN_PROGRESS.dec()
    return response

app = Flask(__name__)


@app.get("/products")
def get_products():
    REQUESTS.labels('products', 'get').inc()
    return "product"


@app.post("/products")
def create_product():
    REQUESTS.labels('products', 'post').inc()
    return "created product", 201


@app.get("/cart")
