from flask import request, jsonify

from project import app
from services.projects import create_project


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
