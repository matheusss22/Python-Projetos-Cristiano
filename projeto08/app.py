from flask import Flask, render_template, request, redirect, url_for
from paciente import Paciente

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/principal")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/calcularIMC", methods=["GET", "POST"])
def calcularIMC():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        peso = request.form.get("peso")
        altura = request.form.get("altura")

        paciente = Paciente(nome, idade, peso, altura)
        
        return render_template("registrosIMC.html", paciente=paciente)

    return render_template("/principal")

if __name__ == "__main__":
    app.run(debug=True)
