from flask import Flask, request, jsonify
from time import sleep
from flask_cors import CORS

from models import db, Contenido

app = Flask(__name__)
CORS(app)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/pelis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/contenidos", methods = ["GET"])
def contenidos():
    try: 
        contenidos = Contenido.query.all()
        contenidos_data = []
        for contenido in contenidos:
            contenido_data = {
                'id':contenido.id,
                'nombre':contenido.nombre,
                'genero':contenido.genero,
                'fecha de lanzamiento': contenido.fecha_lunch,
                'plataforma': contenido.donde_ver,
                'tipo': contenido.peli_o_serie,
                'kids': contenido.kids,
                'imagen': contenido.imagen,
                'estado' : contenido.estado,
            }
            contenidos_data.append(contenido_data)
        return (jsonify(contenidos_data))
    except:
        return(jsonify("No hay elementos"))


@app.route("/contenidos/<id_contenido>", methods = ["GET"])
def data(id_contenido):
    try:
        contenido= Contenido.query.get(id_contenido)
        contenido_data = {
            'id':contenido.id,
            'nombre': contenido.nombre,
            'genero': contenido.genero,
            'fecha': contenido.fecha_lunch,
            'plataforma': contenido.donde_ver,
            'tipo': contenido.peli_o_serie,
            'kids':contenido.kids,
            'imagen': contenido.imagen,
            'estado' : contenido.estado,
        }
        return jsonify(contenido_data)
    except:
        return(jsonify("No se ha encontrado este elemento"))

@app.route("/contenidos/<id_contenido>", methods = ["DELETE"])
def borrar(id_contenido):
    try:
        if Contenido.query.get(id_contenido) == None:
            return{"success": False}
        data = Contenido.query.get(id_contenido)
        db.session.delete(data)
        db.session.commit()
        return{"success": True}
    except:
        return{"success": False}


@app.route("/contenidos", methods = ["POST"])
def nuevo_contenido():
    try: 
        mayor = 0
        contenidos = Contenido.query.all()
        for datos in contenidos:
            if datos.id > mayor:
                mayor=datos.id
        id=mayor+1
        data= request.json
        nuevo_nombre = data.get('nombre')
        nuevo_genero = data.get('genero')
        nueva_fecha_lunch = data.get('fecha')
        nueva_plataforma = data.get('plataforma')
        nuevo_tipo = data.get ('tipo')
        nueva_imagen = data.get('imagen')
        kids = data.get('kids')
        if kids == '0':
            nuevo_kids = False
        elif kids == '1':
            nuevo_kids = True
    
        nuevo_estado = '2'
        nuevo_contenido = Contenido(id=id, nombre=nuevo_nombre, genero = nuevo_genero, fecha_lunch = nueva_fecha_lunch, 
        donde_ver = nueva_plataforma, peli_o_serie = nuevo_tipo, kids = nuevo_kids, imagen = nueva_imagen, estado=nuevo_estado), 
        for item in nuevo_contenido:
            db.session.add(item)
            db.session.commit()
        return {"success": True}
    
    except:
        return {"success": True}

@app.route("/contenidos/<id_contenido>", methods = ["PUT"])
def modificar_contenido(id_contenido):   
    try: 
        contenido= Contenido.query.get(id_contenido)
        data = request.json
        nuevo_estado = data.get('estado')
        contenido.estado = nuevo_estado
        db.session.commit()
        return {"success": True}
    except:
     return {"success": False}
    
@app.route("/contenidos/edit/<id_contenido>", methods = ["PUT"])
def modificar_todo_contenido(id_contenido):   
    try: 
        contenido= Contenido.query.get(id_contenido)
        data = request.json
        nuevo_nombre = data.get('nombre')
        nuevo_genero = data.get('genero')
        nueva_fecha_lunch = data.get('fecha')
        nueva_plataforma = data.get('plataforma')
        nuevo_tipo = data.get ('tipo')
        nueva_imagen = data.get('imagen')
        kids = data.get('kids')

        if kids == '0':
            nuevo_kids = False
        elif kids == '1':
            nuevo_kids = True

        contenido.nombre = nuevo_nombre
        contenido.peli_o_serie = nuevo_tipo
        contenido.genero = nuevo_genero
        contenido.fecha_lunch = nueva_fecha_lunch
        contenido.donde_ver = nueva_plataforma
        contenido.imagen = nueva_imagen
        contenido.kids = nuevo_kids
        db.session.commit()
        return {"success": True}
    except:
     return {"success": False}
    
@app.route("/kids", methods = ["GET"])
def contenidos_kids():
    try: 
        contenidos_kids = Contenido.query.where(Contenido.kids == True).all()
        contenidos_data_kids = []
        for kid in contenidos_kids:
            contenido_data = {
                'id':kid.id,
                'nombre':kid.nombre,
                'genero':kid.genero,
                'fecha de lanzamiento': kid.fecha_lunch,
                'plataforma': kid.donde_ver,
                'tipo': kid.peli_o_serie,
                'kids': kid.kids,
                'imagen': kid.imagen,
                'estado' : kid.estado,
            }
          
            contenidos_data_kids.append(contenido_data)
        return (jsonify(contenidos_data_kids))
    except:
        return(jsonify("No hay elementos"))    
    
@app.route("/peliculas", methods = ["GET"])
def contenidos_pelis():
    try: 
        contenidos_pelis= Contenido.query.where(Contenido.peli_o_serie == 0).all()
        contenidos_data_pelis = []
        for peli in contenidos_pelis:
            contenido_data = {
                'id':peli.id,
                'nombre':peli.nombre,
                'genero':peli.genero,
                'fecha de lanzamiento': peli.fecha_lunch,
                'plataforma': peli.donde_ver,
                'tipo': peli.peli_o_serie,
                'kids': peli.kids,
                'imagen': peli.imagen,
                'estado' : peli.estado,
            }
          
            contenidos_data_pelis.append(contenido_data)
        return (jsonify(contenidos_data_pelis))
    except:
        return(jsonify("No hay elementos"))    
    
@app.route("/series", methods = ["GET"])
def contenidos_series():
    try: 
        contenidos_series= Contenido.query.where(Contenido.peli_o_serie == 1).all()
        contenidos_data_series = []
        for serie in contenidos_series:
            contenido_data = {
                'id':serie.id,
                'nombre':serie.nombre,
                'genero':serie.genero,
                'fecha de lanzamiento': serie.fecha_lunch,
                'plataforma': serie.donde_ver,
                'tipo': serie.peli_o_serie,
                'kids': serie.kids,
                'imagen': serie.imagen,
                'estado' : serie.estado,
            }
          
            contenidos_data_series.append(contenido_data)
        return (jsonify(contenidos_data_series))
    except:
        return(jsonify("No hay elementos")) 
    
@app.route("/lista", methods = ["GET"])
def contenidos_lista():
    try: 
        contenidos_lista= Contenido.query.where(Contenido.estado != 2).all()
        contenidos_data_lista = []
        for i in contenidos_lista:
            contenido_data = {
                'id':i.id,
                'nombre':i.nombre,
                'genero':i.genero,
                'fecha de lanzamiento': i.fecha_lunch,
                'plataforma': i.donde_ver,
                'tipo': i.peli_o_serie,
                'kids': i.kids,
                'imagen': i.imagen,
                'estado' : i.estado,
            }
          
            contenidos_data_lista.append(contenido_data)
        return (jsonify(contenidos_data_lista))
    except:
        return(jsonify("No hay elementos")) 
    

if __name__ == '__main__':
    print('starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('started...')
    
