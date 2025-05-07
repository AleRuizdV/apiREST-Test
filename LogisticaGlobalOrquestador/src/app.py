from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from orquestador.orquestador_service import orquestar_servicio, obtener_informacion_servicio

load_dotenv()

app = Flask(__name__)

@app.route('/orquestar', methods=['POST'])
def route_orquestar_servicio():
    return orquestar_servicio()

@app.route('/informacion-servicio/<string:id>', methods=['GET'])
def route_obtener_informacion_servicio(id):
    return obtener_informacion_servicio(id)

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "¡Hola desde la API de Logística Global!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"))