cfrom flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contenido(db.Model):
    __tablename__= 'contenidos'
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), db.ForeignKey('generos.id'))
    fecha_lunch = db.Column(db.Integer, nullable = False)
    donde_ver = db.Column(db.String(100), db.ForeignKey('plataformas.id'))
    kids = db.Column(db.Boolean)
    peli_o_serie = db.column (db.String(50),db.ForeignKey('pelis_o_series.id'))


class Genero(db.Model):
    __tablename__= 'generos'
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
class Plataforma(db.Model):
    __tablename__= 'plataformas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cuota_mensual = db.Column(db.Integer, nullable = False)

class Peli_o_serie(db.Model):
    __tablename__= 'pelis_o_series'
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    