#!/usr/bin/python3
"""Initialize flask functions"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def view_status():
    """Returns a JSON"""
    response = jsonify({"status": "OK"})
    response.headers["Content-Type"] = "application/json"
    return response
