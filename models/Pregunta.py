from utils.extensions import db 

class Pregunta(db.Model):
    __tablename__ = "preguntas"

    id_pregunta = db.Column(db.String(12), primary_key=True)
    id_test = db.Column(db.String(12), db.ForeignKey("tests.id_test"), nullable=False)
    texto_pregunta = db.Column(db.String(255), nullable=False)

    def __init__(self, id_test, texto_pregunta):
        self.id_test = id_test
        self.texto_pregunta = texto_pregunta

    def to_dict(self):
        return {
            "id_pregunta": self.id_pregunta,
            "id_test": self.id_test,
            "texto_pregunta": self.texto_pregunta
        }
