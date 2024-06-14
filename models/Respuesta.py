from utils.extensions import db 

class Respuesta(db.Model):
    __tablename__ = "respuestas"

    id_respuesta = db.Column(db.String(12), primary_key=True)
    id_pregunta = db.Column(db.String(12), db.ForeignKey("preguntas.id_pregunta"), nullable=False)
    id_usuario = db.Column(db.String(12), db.ForeignKey("usuarios.id_usuario"),nullable=False)
    respuesta = db.Column(db.Integer, nullable=False, default=False)

    def __init__(self, id_pregunta, id_usuario, respuesta=False):
        self.id_pregunta = id_pregunta
        self.id_usuario = id_usuario
        self.respuesta = respuesta

    def to_dict(self):
        return {
            "id_respuesta": self.id_respuesta,
            "id_pregunta": self.id_pregunta,
            "id_usuario": self.id_usuario,
            "respuesta": self.respuesta
        }
