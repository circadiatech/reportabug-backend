from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object("project.config.dev")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

import controllers.notes
import controllers.projects

@app.route("/")
def hello_world():
    return jsonify(hello="world")

if __name__ == '__main__':
	app.run()