from flask import request, jsonify

from project import app
from services.projects import fetch_all_projects


@app.route('/projects', methods=['GET'])
def get_all_projects():
    return jsonify(fetch_all_projects())
