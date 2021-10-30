from flask import request, jsonify

from project import app
from services.projects import fetch_all_projects, fetch_project, delete_project, create_project


@app.route('/projects', methods=['POST'])
def create_projects():
    data = request.get_json()
    if not 'title' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'title of projects is not given'
        }), 400
    project = create_project(data)
    return project


@app.route('/projects', methods=['GET'])
def get_all_projects():
    return jsonify(fetch_all_projects())


@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    return fetch_project(id)


@app.route('/projects/<id>', methods=["DELETE"])
def remove_project(id):
    return delete_project(id)

