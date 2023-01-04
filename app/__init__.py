# app/__init__.py

from flask import Flask
#from flask_session import Session




def create_app():
    app = Flask(__name__)

    from app import routes

    app.secret_key = '070791'
    app.register_blueprint(routes.bp)
    #app.config['SESSION_TYPE'] = 'filesystem'
    #Session(app)

    return app
