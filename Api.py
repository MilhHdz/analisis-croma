from flask import Flask, request, redirect, url_for, send_from_directory
from flask_cors import CORS

from src.Croma import Croma

import os
import time

UPLOAD_FOLDER = os.path.abspath("./uploads/")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "El campo esta vacio"

        f = request.files["ourfile"]

        if f.filename == "":
            return "Ningun archivo seleccionado"

        extencion = f.filename.split(".")
        filename = "time_" + time.strftime("%b") + time.strftime("%d") + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M") + "_" + time.strftime("%S") + "." + extencion[1]

        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        #Tiempo de inicio
        Tiempo_de_Inicio = time.time()

        croma = Croma()
        valor = croma.obtener_Caracteristicas(filename)
        print(valor)
        # Array_Colores, Array_Porcentaje = DC.main(filename)
        

        # print( f'\n\n Tiempo de ejecucion = {time.time() - Tiempo_de_Inicio}' )

        respuesta = f'Nombre: {filename} el tiempo de respuesta es: {time.time() - Tiempo_de_Inicio}'

        return respuesta # filename #filename + str(valor)  #redirect(url_for("get_file", filename=filename))

    return """
    <form method="POST" enctype="multipart/form-data">
    <input type="file" name="ourfile">
    <input type="submit" name="UPLOAD">
    </form>
    """

if __name__ == "__main__":
    app.run()