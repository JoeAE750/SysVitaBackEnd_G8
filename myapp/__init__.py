import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sysvitadb_user:NBBRKfOPt4enLTkMZrcrWjTUzsGd5FRO@dpg-cpal71v109ks73aq24s0-a.oregon-postgres.render.com/sysvitadb"
    # "postgres://sysvitadb_user:NBBRKfOPt4enLTkMZrcrWjTUzsGd5FRO@dpg-cpal71v109ks73aq24s0-a.oregon-postgres.render.com/sysvitadb"

    db.init_app(app)

    app.register_blueprint(main)

    return app