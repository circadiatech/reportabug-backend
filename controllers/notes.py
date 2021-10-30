from flask import request, jsonify

from project import app
from services.notes import read_all_notes, read_one_note, create_note, update_note, delete_note


@app.route('/notes/')
def get_notes():
    return jsonify(read_all_notes())


@app.route('/notes/<id>')
def get_note(id):
    return read_one_note(id)


@app.route('/notes/', methods=['POST'])
def create_notes():
    data = request.get_json()
    if not 'title' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'title of notes is not given'
        }), 400
    note = create_note(data)
    return note


@app.route('/notes/<id>', methods=['PUT'])
def update_notes(id):
    data = request.get_json()
    if not 'title' in data or not 'completed' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'title or completed fields need to be present'
        }), 400
    note = update_note(id, data)
    return note


@app.route('/notes/<id>', methods=['DELETE'])
def delete_notes(id):
    result = delete_note(id)
    return result
