from flask import Flask, jsonify, request
from waitress import serve

import subprocess
import socket

app = Flask(__name__)


def get_config(val):
    stdout, _ = subprocess.Popen(
        ["snapctl", "get", val], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).communicate()
    o = stdout.decode("utf-8").strip()
    return o


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    send_tcp(str(data))
    return jsonify({})


def send_tcp(data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", int(get_config("dest-port"))))
        s.sendall(bytes(data, encoding="utf-8"))
    finally:
        s.close()


def main():
    serve(app, host="0.0.0.0", port=get_config("src-port"), threads=8)
