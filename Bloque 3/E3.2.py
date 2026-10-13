"""Carga iris.csv con DictReader, convierte las medidas a float
y calcula la media por clase."""
import csv 
from pathlib import Path


RUTA= Path(__file__).parent / "iris.csv"
MEDIDAS= ['largo_sep'],['ancho_sep'],['largo_pet'],['ancho_pet']


with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))


def obtener_media_columna(filas,columna):
    valores={}
    for fila in filas:
        clase=fila["clase"]

        if clase not in valores:
            valores[clase]=[]
        valores[clase].append(fila[columna])
    print(valores)

    resultados={}
    for clase,v in valores.items():
        resultados[clase]=round(sum(v)/len(v),2)
    print(resultados)
    
    return resultados


for fila in filas:
    for medida in MEDIDAS:
        fila[medida]=float(fila[medida])
