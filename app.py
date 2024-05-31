import os

from flask import Flask 

from utils.extensions import db
from routes.Usuarios_routes import Usuario_routes

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    # "postgresql://sysvitadb_user:NBBRKfOPt4enLTkMZrcrWjTUzsGd5FRO@dpg-cpal71v109ks73aq24s0-a.oregon-postgres.render.com/sysvitadb"

    db.init_app(app)

    app.register_blueprint(Usuario_routes)

    return app