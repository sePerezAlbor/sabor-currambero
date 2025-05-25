from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

from app import db

# ----------------------
# Clase Usuario
# ----------------------

class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(50), nullable=False)
    segundo_nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50), unique=True, nullable=False)
    contrasenia = db.Column(db.String(50), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    rol = db.Column(db.Enum('cliente', 'admin'), nullable=False)

    # ✅ Fija la relación indicando qué clave usar
    perfil = db.relationship('PerfilGastronomico', backref='usuario', uselist=False)
    def get_id(self):
        return str(self.id_usuario)





# ----------------------
# Clase Perfil Gastronómico
# ----------------------
class PerfilGastronomico(db.Model):
    __tablename__ = 'Perfil_Gastronomico'

    id_perfil = db.Column(db.Integer, primary_key=True)  # nueva clave primaria
    tipo_comida_fav = db.Column(db.String(100))
    restricciones = db.Column(db.Text, nullable=False)
    presupuesto_promedio = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), unique=True, nullable=True)





# ----------------------
# Clase Restaurante
# ----------------------
class Restaurante(db.Model):
    __tablename__ = 'Restaurante'

    id_restaurante = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    tipo_comida = db.Column(db.String(100), nullable=False)
    precio_promedio = db.Column(db.Integer, nullable=False)
    latitud = db.Column(db.Numeric(9, 6))
    longitud = db.Column(db.Numeric(9, 6))
    calificacion_prom = db.Column(db.Numeric(2, 1), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    instagram = db.Column(db.String(50))

    valoraciones = db.relationship('Valoracion', backref='restaurante', lazy=True)
    visitas = db.relationship('Visita', backref='restaurante', lazy=True)
    favoritos = db.relationship('Favorito', backref='restaurante', lazy=True)


# ----------------------
# Clase Valoración
# ----------------------
class Valoracion(db.Model):
    __tablename__ = 'Valoracion'

    id_valoracion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Enum('1', '2', '3', '4', '5'), nullable=False)
    comentario = db.Column(db.Text)
    fecha_valoracion = db.Column(db.Date)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    id_restaurante = db.Column(db.Integer, db.ForeignKey('Restaurante.id_restaurante'), nullable=False)


# ----------------------
# Clase Visita
# ----------------------
class Visita(db.Model):
    __tablename__ = 'Visita'

    id_visita = db.Column(db.Integer, primary_key=True)
    fecha_visita = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    id_restaurante = db.Column(db.Integer, db.ForeignKey('Restaurante.id_restaurante'), nullable=False)


# ----------------------
# Clase Favorito
# ----------------------
class Favorito(db.Model):
    __tablename__ = 'Favorito'

    fecha_agregado = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), primary_key=True)
    id_restaurante = db.Column(db.Integer, db.ForeignKey('Restaurante.id_restaurante'), primary_key=True)
