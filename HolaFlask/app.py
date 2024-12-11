## Importamos flask
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HOLAFLASK():
    return "<h1>¡Hola flask!</h1> <hr>"

## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tiene un valor de
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

## Tomamos la tercera ruta y la reemplazamos pr el siguiente wjwmplo
## 2.) un progrma que al capturar la edad de una persona deiga si es:
## menor de edad (menor a 18 años)
## adulto (mayor o igual a 18 años y menor a 60 años)
## adulto mayor (mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>la persona es: {R}</h1> <hr>"

## creamos otra ruta relaizamos el siguiente ejemplo
## 3.) programa que crea arreglos con valores aletorios 
## Importamos la libreria numpy si no existe la instalamos con:pip install numpy
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1>El arreglo aletorio es: {arreglo}</h1> <hr>"

if __name__=='main_':
    ## El valor true indica que la app se deja en modo debug
    app.run(debug=True)
    