from utils.extensions import db 

class Resultados(db.Model):
    __tablename__ = "resultados"

    id_resultado = db.Column(db.String(12), primary_key=True)
    id_test = db.Column(db.String(12), db.ForeignKey("tests.id_test"), nullable=False)
    id_usuario = db.Column(db.String(12), db.ForeignKey("usuarios.id_usuario"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    fecha_realizacion = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, id_test, id_usuario, score):
        self.id_test = id_test
        self.id_usuario = id_usuario
        self.score = score

    def to_dict(self):
        return {
            "id_resultado": self.id_resultado,
            "id_test": self.id_test,
            "id_usuario": self.id_usuario,
            "score": self.score,
            "fecha_realizacion": self.fecha_realizacion.strftime("%Y-%m-%d %H:%M:%S")
        }
