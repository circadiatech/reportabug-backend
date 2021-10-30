from flask import request, jsonify

from project import app
from services.projects import fetch_all_projects, fetch_project, delete_project


@app.route('/projects', methods=['GET'])
def get_all_projects():
    return jsonify(fetch_all_projects())


@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    return fetch_project(id)


@app.route('/projects/<id>', methods=["DELETE"])
def remove_project(id):
    return delete_project(id)
