from flask import Blueprint, jsonify,request

from utils.extensions import db
from models.Usuario import *
from models.Facultad import Facultad

Usuarios_routes = Blueprint("Usuarios_routes", __name__)

@Usuarios_routes.route("/usuarios", methods=["POST"])
def add_usuario():
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    id_facultad = data.get("id_facultad")
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    fecha_nac = data.get("fecha_nac")
    genero = data.get("genero")
    dni = data.get("dni")
    email = data.get("email")
    contrasena = data.get("contrasena")

    if not all([id_usuario, id_facultad, nombre, apellido, fecha_nac, genero, dni, email, contrasena]):
        return jsonify({"message": "Todos los campos son requeridos", "status": "error"}), 400

    new_usuario = Usuario(id_usuario=id_usuario, id_facultad=id_facultad, nombre=nombre, apellido=apellido, 
                          fecha_nac=fecha_nac, genero=genero, dni=dni, email=email, contrasena=contrasena)
    db.session.add(new_usuario)
    db.session.commit()

    return jsonify({"message": "Usuario creado", "status": "exito", "usuario": new_usuario.to_dict()}), 201

@Usuarios_routes.route("/usuarios/email/<string:email>", methods=["GET"])
def get_usuario_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        return jsonify(usuario.to_dict()), 200
    else:
        return jsonify({"message": "Usuario not found", "status": "error"}), 404

@Usuarios_routes.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200