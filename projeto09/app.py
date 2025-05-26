from flask import Flask, render_template, request, redirect
from projeto_calcada import Projeto_Calcada

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/principal")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        try:
            largura_terreno = request.form.get("largura_terreno")
            profundidade_terreno = request.form.get("profundidade_terreno")
            largura_calcada = request.form.get("largura_calcada")
            altura_concreto = request.form.get("altura_concreto")

            projeto = Projeto_Calcada(largura_terreno, profundidade_terreno, largura_calcada, altura_concreto)

            return render_template("metricas.html", error=False, projeto=projeto)

        except ValueError as e:
            return render_template("principal.html", error=True, message=str(e))

    return render_template("principal.html")

if __name__ == "__main__":
    app.run(debug=True)
