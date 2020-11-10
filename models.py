from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

class Usuario(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column(db.String(70))
    last_name = db.Column(db.String(70))
    username = db.Column(db.String(70),unique=True)
    contrasena = db.Column(db.String(70))

class Clientes(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column(db.String(70))
    last_name = db.Column(db.String(70))
    username = db.Column(db.String(70),unique=True)
    contrasena = db.Column(db.String(70))
    tipo=db.Column(db.String(70))

class Receta(UserMixin,,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Titulo = db.Column(db.String(70))
    Resumen = db.Column(db.String(120))
    Ingredientes = db.Column(db.String(80))
    Preparacion = db.Column(db.String(80))
    Tiempo_preparacion = db.Column(db.String(20))
    Imagenes = db.Column(db.String(80))
    ver = db.Column(db.String(120))
    comentario = db.Column(db.String(120))
    comentario_fecha = db.Column(db.String(120))
    comentario_titulo=db.Column(db.String(120))
    reaccion = db.Column(db.String(70))

    questions_asked = db.relationship(
        'Question', 
        foreign_keys='Question.asked_by_id', 
        backref='asker', 
        lazy=True
    )

    answers_requested = db.relationship(
        'Question',
        foreign_keys='Question.expert_id',
        backref='expert',
        lazy=True
    )

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)


