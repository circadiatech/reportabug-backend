from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from database import db


app = Flask(__name__)
app.config.from_object("project.config.dev")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

import controllers.notes

@app.route('/project/<id>', methods=['DELETE'])
def delete(self):
    data = RequestCacheControl.get_json()
    task = data["task"]
    obj = Task_Model.find_by_name(task)
    
    if obj is None:
            return make_response(jsonify({
                "Msg": "Task Does not exist",
                "Status": 404
            }),404)
        
    obj.delete_from_db()
    
    return make_response(jsonify({
            "Msg": "Task Deleted",
            "Status": 202
        }),202)

if __name__ == '__main__':
	app.run()