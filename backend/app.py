from flask import Flask, request, jsonify
from time import sleep
from flask_cors import CORS

from models import db, Contenido

app = Flask(__name__)
CORS(app)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/pelis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def hello_world():
    return 'HOLA'

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


@app.route("/contenidos", methods = ["POST"])
def nuevo_contenido():
    try: 
        data= request.json
        nuevo_nombre = data.get('nombre')
        nuevo_genero = data.get('genero')
        nueva_fecha_lunch = data.get('fecha de lanzamiento')
        nueva_plataforma = data.get('plataforma')
        nuevo_tipo = data.get ('tipo')
        nuevo_kids = data.get ('kids')
        nuevo_contenido = Contenido(nombre=nuevo_nombre, genero = nuevo_genero, fecha_lunch = nueva_fecha_lunch, 
        donde_ver = nueva_plataforma, tipo = nuevo_tipo, kids = nuevo_kids),201
        db.session.add(nuevo_contenido)
        db.session.commit()

        return (jsonify({'contenido':{'id':nuevo_contenido.id, 'nombre': nuevo_contenido.nombre, 
        'genero':nuevo_contenido.genero, 'fecha de lanzamiento': nuevo_contenido.fecha_lunch, 
        'plataforma donde ver': nuevo_contenido.donde_ver, 'tipo': nuevo_contenido.peli_o_serie, 
        'kids':nuevo_contenido.kids }}))
    
    except Exception as error:
        print(error)
        return (jsonify("no se pudo agregar el nuevo contenido")),500

@app.route("/contenidos", methods = ["PUT"])
def modificar_contenido():
    id = request.json.get("id")
    name = request.json.get("name")
    names = request.json.get("names")
    publisher = request.json.get("publisher")
    gender = request.json.get("gender")
    alignment = request.json.get("alignment")
    image = request.json.get("image")
    race = request.json.get("race")

    character = {
        "id": id,
        "name": name,
        "names": names,
        "publisher": publisher,
        "gender": gender,
        "alignment": alignment,
        "image": image,
        "race": race
    }
    return {"success": "id"}

if __name__ == '__main__':
    print('starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('started...')
    
