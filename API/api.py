from flask import Flask, request, jsonify
from collections import defaultdict
import jwt
import json
import time
from uuid import uuid4
app = Flask(__name__)

# Desactiva el uso del token
debug_mode = True

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
		},
		"0fecb9fa-8e5c-4b6a-831a-32a9bc64f54a":
		{
			"cantidadDiaria": 150,
			"comederosAcceso": {
				"e1750ed4-59e0-4ca4-ab91-d8b1123377bb": True
			},
			"estado": "Enfermo",
			"foto": "",
			"nombre": "Antonio",
			"observaciones": {
					"9ada8af2-d7d3-4fb0-a09e-f1d2ba271bc2": {"mensaje": "Ha llegado al límite diario"}
			},
			"pienso": "TensorFood",
			"tipo": "Perro"
		}
	},
	"comederos": {
		"e1750ed4-59e0-4ca4-ab91-d8b1123377bb": {
			"nombre": "Cocina",
			"ultimaRecarga": 1553203380,
			"comidaCargada": 500,
			"nivelComida": 100,
			"nivelAgua": 50,
			"aguaCargada": 150,
			"registros": {
				"3765815a-4303-49bd-9063-cc775c90c3b7": {
					"fecha": 1553271048,
					"generadoPor": "95bf8d4d-beb0-4163-9bc8-febdeba1fa5f",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 25
					}
				},
				"cca88d90-8aa5-4784-a7fa-7fe0508671d6": {
					"fecha": 1553203380,
					"generadoPor": "95bf8d4d-beb0-4163-9bc8-febdeba1fa5f",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 10
					}
				},
				"3775cf5a-3f0b-4bfc-8ad5-fd1d2ea20870": {
					"fecha": 1553171640,
					"generadoPor": "95bf8d4d-beb0-4163-9bc8-febdeba1fa5f",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 20
					}
				},
				"650f819c-8d39-4959-86e6-10af2526b5a9": {
					"fecha": 1553142192,
					"generadoPor": "95bf8d4d-beb0-4163-9bc8-febdeba1fa5f",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 15
					}
				},
				"301cbc55-9ccd-4cd1-99fe-31d9e931c2e2": {
					"fecha": 1553052002,
					"generadoPor": "e1750ed4-59e0-4ca4-ab91-d8b1123377bb",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 10
					}
				},
				"5811e419-bfe6-4e85-94a1-a550b65fcabe": {
					"fecha": 1553092440,
					"generadoPor": "e1750ed4-59e0-4ca4-ab91-d8b1123377bb",
					"tipoRegistro": "0",
					"datos": {
						"comidaConsumida": 20
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
	# Evitamos tener que enviar el token en la rama de desarrollo
    if debug_mode:
        response = {"status": 200, "response": datos}
	#Comprobamos que las credenciales son válidas
    if "Authorization" in request.headers.keys():
        if request.headers["Authorization"] != "":
            username = jwt.decode(request.headers["Authorization"], 'HackForGood', algorithms=['HS256'])["username"]
            if username in credenciales.keys():
				# Devolvemos los datos del usuario, en este caso los datos dummy
                response = {"status": 200, "response": datos}
    return jsonify(response)


# Tal como está diseñado permite modificar o añadir animales
@app.route("/api/animal/modificarAnimal", methods=["POST"])
def modificarAnimal():
    datosAnimal = request.get_json(silent=True)

	# Evitamos tener que enviar el token en la rama de desarrollo
    if debug_mode:
        for key in datosAnimal.keys():
			# Cambiamos los datos del usuario
            datos["ErManu"]["animales"][key] = datosAnimal[key]
        response = {"status": 200, "response": {}}
    
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
# Idem
@app.route("/api/animal/modificarComedero", methods=["POST"])
def modificarComedero():
    datosComedero = request.get_json(silent=True)

	# Evitamos tener que enviar el token en la rama de desarrollo
    if debug_mode:
        for key in datosComedero.keys():
			# Cambiamos los datos del usuario
            datos["ErManu"]["comederos"][key] = datosComedero[key]
        response = {"status": 200, "response": {}}
    
    response = {"status": 403, "response": {}}
    if "Authorization" in request.headers.keys():
        if request.headers["Authorization"] != "":
            username = jwt.decode(request.headers["Authorization"],	 'HackForGood', algorithms=['HS256'])["username"]
            if username in credenciales.keys():
                for key in datosComedero.keys():
					# Cambiamos los datos del usuario
                    datos[username]["comederos"][key] = datosComedero[key]
                response = {"status": 200, "response": {}}


    return jsonify(response)

app.run()