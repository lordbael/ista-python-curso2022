from flask import Flask, request
import csv
import json


app = Flask(__name__)


@app.route('/')
def index():
    return 'Listado de Estudiantes'


@app.route('/estudiantes', methods=['GET']) #Obtener datos y estudiantes por un get
def lista_estudiantes():
    with open('datos\estudiante.csv') as file:
        reader = csv.reader(file)
        next(reader)
        lista = []
        for columna in reader:
            lista.append({
                'cedula': columna[0],
                'primer_apellido': columna[1],
                'segundo_apellido': columna[2],
                'primer_nombre': columna[3],
                'segundo_nombre': columna[4]
            })
    return json . dumps(sorted(lista, key=lambda x: x['cedula']))


@app.route('/registrar_asistencia', methods=['POST']) #Crear datos y estudiantes por medio de un post mapping
def registrar_asistencia():
    with open('datos\asistencia.csv', 'a', newline='') as listado:
        writer = csv.writer(listado, delimiter=',', quotechar='',
                            quoting=csv.QUOTE_NONE, escapechar=' ')
        guardado = [request.json['cedula']+',' + request.json['materia']+',' +
                    request.json['fecha_año']+',' + request.json['fecha_mes']+',' + request.json['fecha_dia']]
        writer.writerow(guardado)
    return 'Los Datos se han guardado'


if __name__ == '__main__':
    app.run(debug=True)
