import os
import logging
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

metrics = PrometheusMetrics(app)

metrics.info("app_info", "CloudNative Pipeline application info", version="1.0.0")


@app.route("/")
def home():
    logger.info("Home endpoint called")
    return jsonify({
        "app": "cloudnative-pipeline",
        "version": "1.0.0",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


@app.route("/api/v1/items")
def get_items():
    logger.info("Items endpoint called")
    items = [
        {"id": 1, "name": "item-one", "category": "demo"},
        {"id": 2, "name": "item-two", "category": "demo"},
        {"id": 3, "name": "item-three", "category": "demo"},
    ]
    return jsonify({"items": items, "count": len(items)})


@app.route("/api/v1/items/<int:item_id>")
def get_item(item_id):
    logger.info(f"Item {item_id} requested")
    if item_id < 1 or item_id > 3:
        return jsonify({"error": "item not found"}), 404
    return jsonify({"id": item_id, "name": f"item-{item_id}", "category": "demo"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    logger.info(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=debug)
