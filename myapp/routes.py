from flask import Blueprint, redirect, url_for

from .extensions import db
from .models import Facultad

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = Facultad.query.all()
    users_list_html = [f"<li>{ user.nombre }</li>" for user in users]
    return f"<ul>{''.join(users_list_html)}</ul>"

@main.route('/add/<username>')
def add_user(username):
    db.session.add(Facultad(id_facultad=1,nombre=username))
    db.session.commit()
    return redirect(url_for("main.index"))