import os
from flask import Flask     # jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# instantiate the db
db = SQLAlchemy()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # enable CORS
    CORS(app)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    with app.app_context():
        db.create_all()

    return app
