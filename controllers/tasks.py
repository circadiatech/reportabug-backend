from flask import request, jsonify

from project import app
from services.tasks import fetch_task


@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    return fetch_task(id)
