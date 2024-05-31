from flask import Blueprint, redirect, url_for

from utils.extensions import db
from models.Facultad import Facultad

Facultad_routes = Blueprint('Facultad_routes', __name__)


@Facultad_routes.route('/Facultad')
def add_user(username):
    db.session.add(Facultad(id_facultad=100,nombre=username))
    db.session.commit()
    return redirect(url_for("main.index"))