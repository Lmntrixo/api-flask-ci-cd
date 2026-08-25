from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    return jsonify(version="1.0.0"), 200


@app.route("/caline")
def version():
    return jsonify(version="i love you more than everything Caline"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
