from utils.extensions import db 

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.String(12), primary_key=True)
    id_facultad = db.Column(db.Integer, db.ForeignKey('facultades.id_facultad'))
    nombre = db.Column(db.String(32))
    apellido = db.Column(db.String(32))
    fecha_nac = db.Column(db.Date)
    genero = db.Column(db.String(8))
    dni = db.Column(db.String(8))
    email = db.Column(db.String(254))
    contrasena = db.Column(db.String(32))


def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'id_facultad': self.id_facultad,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nac': self.fecha_nac.strftime('%Y-%m-%d'),
            'genero': self.genero,
            'dni': self.dni,
            'email': self.email
        }