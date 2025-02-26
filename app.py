from flask import Flask, request, redirect, url_for, render_template
from lector import read_csv
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No se seleccionó ningún archivo"

    file = request.files["file"]

    if file.filename == "":
        return "Nombre de archivo vacío"

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)  # Guardar el archivo en la carpeta "uploads"
        return render_template("upload.html", filename=file.filename)
    
    
@app.route('/sorteo/<name_csv>')
def sorteo(name_csv):
    invitados_asistentes =  read_csv(name_csv)
    total = len(invitados_asistentes)
    return render_template('sorteo.html',invitados_asistentes=invitados_asistentes, total = total)



if __name__ == '__main__':
    app.run(debug=True)
