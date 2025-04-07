from flask_login import UserMixin
from . import db
from datetime import datetime

class Cliente(db.Model, UserMixin):
    cliente_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    apellido = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())
    estado = db.Column(db.String(50), default='activo')
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    __table_args__ = {'mysql_auto_increment': '10000'}

    def get_id(self):
        return str(self.cliente_id)