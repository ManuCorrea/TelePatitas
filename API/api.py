from flask import Flask, request, jsonify
from collections import defaultdict
import jwt
import json
import time
from uuid import uuid4
app = Flask(__name__)

# Dummy database
datos = defaultdict(dict)
datos["ErManu"] = {
	"animales": {
		"95bf8d4d-beb0-4163-9bc8-febdeba1fa5f": {
			"nombre": "Neko",
			"estado": "Sano",
			"observaciones": {
				"65bc86d0-a6e9-4d78-bbc5-eaa38748e5e2":
				{
					"mensaje": "Aún no ha comido"
				}
			},
			"tipo": "Gato",
			"foto": "",
			"pienso": "Applaws",
			"cantidadDiaria": 60,
			"comederosAcceso": {
				"e1750ed4-59e0-4ca4-ab91-d8b1123377bb": True
			}
		}
	},
	"comederos": {
		"e1750ed4-59e0-4ca4-ab91-d8b1123377bb": {
			"comidaCargada": 500,
			"nivelComida": 100,
			"nivelAgua": 50,
			"aguaCargada": 150,
			"registros": {
				"3765815a-4303-49bd-9063-cc775c90c3b7": {
					"hora": 1553271048,
					"generadoPor": "95bf8d4d-beb0-4163-9bc8-febdeba1fa5f",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 25
					}
				}
			}
		}
	}
}

#Dummy login
credenciales = {'ErManu': 'TensorGato'}
secret_jwt = "HackForGood"


@app.route("/")
def hi():
    return "Welcome Human"


@app.route("/api/user/login", methods=['POST'])
def login():
    #Dummy Login
    sesion = request.get_json(silent=True)
    response = {"status": 401, "response": {}}
    # Lo siento, no hay hashes hoy
    if sesion != None and "username" in sesion.keys() and "password" in sesion.keys():
        if sesion["username"] in credenciales.keys():
            if credenciales[sesion["username"]] == sesion["password"]:
                # Enviamos un token para identificar a los usuarios en el resto de peticiones
                token =  jwt.encode({'username': sesion["username"], "iat": int(time.time())}, secret_jwt, algorithm='HS256').decode("utf-8") 
                response = {"status": 200, "response": {"token": token}}

    return jsonify(response)

@app.route("/api/user/getData", methods=['GET'])
def getData():
    response = {"status": 403, "response": {}}
	#Comprobamos que las credenciales son válidas
    if "Authorization" in request.headers.keys():
        if request.headers["Authorization"] != "":
            username = jwt.decode(request.headers["Authorization"], 'HackForGood', algorithms=['HS256'])["username"]
            if username in credenciales.keys():
				# Devolvemos los datos del usuario
                response = {"status": 200, "response": datos}
    return jsonify(response)


# Tal como está diseñado permite modificar o añadir animales
@app.route("/api/animal/modificarAnimal", methods=["POST"])
def modificarAnimal():
    datosAnimal = request.get_json(silent=True)
    
    response = {"status": 403, "response": {}}
    if "Authorization" in request.headers.keys():
        if request.headers["Authorization"] != "":
            username = jwt.decode(request.headers["Authorization"], 'HackForGood', algorithms=['HS256'])["username"]
            if username in credenciales.keys():
                for key in datosAnimal.keys():
					# Cambiamos los datos del usuario
                    datos[username]["animales"][key] = datosAnimal[key]
                response = {"status": 200, "response": {}}


    return jsonify(response)


@app.route("/api/animal/modificarComedero", methods=["POST"])
def modificarComedero():
    datosComedero = request.get_json(silent=True)
    
    response = {"status": 403, "response": {}}
    if "Authorization" in request.headers.keys():
        if request.headers["Authorization"] != "":
            username = jwt.decode(request.headers["Authorization"], 'HackForGood', algorithms=['HS256'])["username"]
            if username in credenciales.keys():
                for key in datosComedero.keys():
					# Cambiamos los datos del usuario
                    datos[username]["comederos"][key] = datosComedero[key]
                response = {"status": 200, "response": {}}


    return jsonify(response)

app.run()