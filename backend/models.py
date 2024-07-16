from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contenido(db.Model):
    __tablename__= 'contenidos'
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.Integer, db.ForeignKey('generos.id_genero'))
    fecha_lunch = db.Column(db.Date, nullable = False)
    donde_ver = db.Column(db.Integer, db.ForeignKey('plataformas.id_plataforma'))
    kids = db.Column(db.Boolean)
    peli_o_serie = db.column (db.Integer,db.ForeignKey('pelis_o_series.id_peli_o_serie'))


class Genero(db.Model):
    __tablename__= 'generos'
    id_genero= db.Column(db.Integer, primary_key=True)
    nombre_genero = db.Column(db.String(100), nullable=False)
    
class Plataforma(db.Model):
    __tablename__= 'plataformas'
    id_plataforma = db.Column(db.Integer, primary_key=True)
    nombre_plataforma = db.Column(db.String(100), nullable=False)

class Peli_o_serie(db.Model):
    __tablename__= 'pelis_o_series'
    id_peli_o_serie= db.Column(db.Integer, primary_key=True)
    nombre_peli_o_serie = db.Column(db.String(100), nullable=False)

class Estado(db.Model):
    __tablename__='estados'
    id_estado=db.Column(db.Integer, primary_key=True)
    nombre_estado=db.column(db.String(100), nullable=False)