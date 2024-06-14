from utils.extensions import db 

class Test(db.Model):
    __tablename__ = "tests"

    id_test = db.Column(db.String(12), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id_test": self.id_test,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }
