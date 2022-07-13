from flask import Flask, jsonify

app = Flask(__name__)

def leer_archivo():
    archivo = None
    with open("estudiante.csv") as a:
        archivo = a.readlines()
    return archivo
    
@app.route('/obtener_datos')
def procesar_informacion():
    contenido = leer_archivo()
    partes = contenido[0].split(',')
    return jsonify({"nombre": partes[0], "cedula": partes[1]})