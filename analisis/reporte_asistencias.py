import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos\estudiante.csv')
print('Estudiantes')
print(df)

df1 = pd.read_csv('datos\asistencia.csv')
print('Asistencias')
print(df1)

asistencias = pd.merge(df, df1,  how="right")
print('ASISTENCIAS Y ESTUDIANTES')
print(asistencias)

print('Asistencia y Estudiante mediante cedula de = 0150917169')
print(asistencias[asistencias.cedula == 2233445566])

asistencias[asistencias.cedula == 2233445566].to_csv(
    'reporte_0150917169.csv', index=True)

asistencias[asistencias.cedula ==
            2233445566]['materia'].value_counts().plot(kind='bar')
plt.show()