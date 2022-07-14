from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Juan Carlos Inga</h1>'


@app.route('/read_estudiante')
def read_estudiante():
    with open('datos\estudiante.csv') as archivo:
        reader = csv.reader(archivo)
        next(reader)
        lista_estudiante = []
        for fila in reader:
            lista_estudiante.append({
                'cedula': fila[0], 'primer_apellido': fila[1], 'segundo_apellido': fila[2], 'primer_nombre': fila[3], 'segundo_nombre': fila[4]
            })
    return json.dumps(sorted(lista_estudiante, key=lambda x: x['primer_apellido']))


@app.route('/create_asistencia', methods=['POST'])
def create_asistencia():

    with open('datos\asistencia.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter=',')
        escritor.writerow([request.json['cedula'], request.json['materia'],
                          request.json['fecha_anio'], request.json['fecha_mes'], request.json['fecha_dia']])
    return '<h2>REGISTRO COMPLETADO</h2>'


@app.route('/update_asistencia/<cedula>', methods=['PUT'])
def update_asistencia(cedula):
    with open('datos\asistencia.csv') as file:
        reader = csv.reader(file)
        next(reader)
        lista = []
        for columna in reader:
            lista.append({
                'cedula': columna[0],
                'materia': columna[1],
                'fecha_anio': columna[2],
                'fecha_mes': columna[3],
                'fecha_dia': columna[4]
            })
    for i in lista:
        if i['cedula'] == cedula:
            i['materia'] = request.json['materia']
            i['fecha_anio'] = request.json['fecha_anio']
            i['fecha_mes'] = request.json['fecha_mes']
            i['fecha_dia'] = request.json['fecha_dia']
    with open('datos\asistencia.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['cedula', 'materia', 'fecha_anio',
                        'fecha_mes', 'fecha_dia'])
        for asistencia in lista:
            writer.writerow([asistencia['cedula'], asistencia['materia'],
                            asistencia['fecha_anio'], asistencia['fecha_mes'], asistencia['fecha_dia']])
    return '<h2>REGISTRO ACTUALIZADO</h2>'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='
