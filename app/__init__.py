# app/__init__.py

from flask import Flask




def create_app():
    app = Flask(__name__)

    from app import routes

    app.secret_key = '070791'
    app.register_blueprint(routes.bp)

    return app
