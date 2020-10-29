from flask import Flask, jsonify, request
from waitress import serve

import subprocess
import socket
import json
import os

app = Flask(__name__)


def get_config(val, default=None):
    if int(os.getenv("INDOCKER")) == 1:
        ret = os.getenv(val.replace("-", "_").upper())
    else:
        stdout, _ = subprocess.Popen(
            ["snapctl", "get", val], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ).communicate()
        ret = stdout.decode("utf-8").strip()

    if ret:
        return ret
    return default


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    send_tcp(json.dumps(data))
    return jsonify({})


def send_tcp(data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((get_config("dest-addr", "127.0.0.1"), int(get_config("dest-port"))))
        s.sendall(bytes(data, encoding="utf-8"))
    finally:
        s.close()


def main():
    serve(app, host="0.0.0.0", port=get_config("src-port"), threads=8)
