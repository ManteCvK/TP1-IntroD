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
        contenidos = Contenido.query.all()
        id = int(contenidos[-1].id) + 1
        data= request.json
        nuevo_nombre = data.get('nombre')
        nuevo_genero = data.get('genero')
        nueva_fecha_lunch = data.get('fecha')
        nueva_plataforma = data.get('plataforma')
        nuevo_tipo = data.get ('tipo')
        nueva_imagen = data.get('imagen')
        kids = data.get('estado')
        if kids == 0:
            nuevo_kids = False
        else:
            nuevo_kids = True
            
        nuevo_estado = '2'
        nuevo_contenido = Contenido(id=id, nombre=nuevo_nombre, genero = nuevo_genero, fecha_lunch = nueva_fecha_lunch, 
        donde_ver = nueva_plataforma, peli_o_serie = nuevo_tipo, kids = nuevo_kids, imagen = nueva_imagen, estado=nuevo_estado), 201
        for item in nuevo_contenido:
            db.session.add(item)
            db.session.commit()
        return {"success": True}
    
    except Exception as error:
        print(error)
        return (jsonify("no se pudo agregar el nuevo contenido")),500

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

if __name__ == '__main__':
    print('starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('started...')
    
