# -*- coding: utf-8 -*-

"""
Proxy api.openai.com and returns them (Flask)
"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from flask import Flask, jsonify, request
import uvicorn
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

def create_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

session = create_session()

@app.route("/<path:subpath>", methods=["POST", "GET"])
def conversation(subpath: str):
    if request.headers.get("Authorization") is None:
        return jsonify({"error": "Missing Authorization header"})
    try:
        headers = {
            "Authorization": request.headers.get("Authorization"),
            "Content-Type": "application/json",
        }
        # Send request to OpenAI
        if request.method == "POST":
            response = session.post(
                url="https://api.openai.com/" + subpath,
                headers=headers,
                json=request.get_json(),
                timeout=360,
            )
        if response.status_code == 403:
            return jsonify(
                {
                    "error": "Request expired. Please wait a few minutes while I refresh"
                }
            )
        return response.json()
    except Exception as exc:
        return jsonify({"error": str(exc)})


if __name__ == "__main__":
    # app.run(debug=True)
    uvicorn.run(WsgiToAsgi(app), host="0.0.0.0", port=8080, server_header=False)

