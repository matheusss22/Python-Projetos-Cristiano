from flask import Flask, render_template, request, redirect, url_for
from aluno import Aluno

app = Flask(__name__)

# Banco de dados em memória
banco_alunos = []

@app.route("/")
def home():
    return redirect("principal")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/cadastrarAluno", methods=["GET", "POST"])
def cadastrarAluno():

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")

        aluno = Aluno(nome, email, telefone, senha)
        banco_alunos.append(aluno)

        return render_template("cadastrosAlunos.html", alunos=banco_alunos)


if __name__ == "__main__":
    app.run(debug=True)