from flask import Flask, request, jsonify
from time import sleep

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']=''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")


@app.route("/contenidos")
def data():
    try: 
        elementos = contenido.query.all()
        contenidos_data = []

    except


@app.route("/contenidos/<id_contenido>")
def data(id_contenido):
    try:
        contenido=contenido.query.get(id_contenido)
        contenido_data = {
            'id':contenido.id,
            'nombre': contenido.nombre,
            'genero': contenido.genero,
            'fecha de lanzamiento': contenido.fecha_lunch,
            'plataforma': contenido.donde_ver,
            'tipo': contenido.peli_o_serie,
        }
        return jsonify(contenido_data)
    except:
        return(jsonify("No se ha encontrado este elemento"))

@app.route("/contenidos/<id>", methods = ["DELETE"])


@app.route("/contenidos", methods = ["POST"])
def create_character():
    name = request.json.get("name")
    names = request.json.get("names")
    publisher = request.json.get("publisher")
    gender = request.json.get("gender")
    alignment = request.json.get("alignment")
    image = request.json.get("image")
    race = request.json.get("race")

    id = int(get_all_characters()[-1]["id"]) + 1

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
    return {"success": add_character(character), "id": id}

@app.route("/contenidos", methods = ["PUT"])
def alter_character():
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
    return {"success": edit_character(character), "id": id}

if __name__ == '__main__':
    print('starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('started...')