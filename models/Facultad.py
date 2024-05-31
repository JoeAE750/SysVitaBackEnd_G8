from utils.extensions import db 

class Facultad(db.Model):
    __tablename__ = 'facultades'
    id_facultad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))