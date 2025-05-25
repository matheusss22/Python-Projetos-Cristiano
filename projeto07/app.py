from flask import Flask, render_template, request, redirect, url_for
from livro import Livro

app = Flask(__name__)

# Banco de dados em memória para livros
banco_livros = []

@app.route("/")
def home():
    return redirect("/principal")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/cadastrarLivro", methods=["GET", "POST"])
def cadastrarLivro():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        ano_publicacao = request.form.get("ano_publicacao")

        livro = Livro(titulo, autor, ano_publicacao)
        banco_livros.append(livro)

        return render_template("cadastrosLivros.html", livros=banco_livros)

    return render_template("cadastrosLivros.html", livros=banco_livros)

@app.route("/buscarLivro", methods=["GET"])
def buscarLivro():
    titulo_procurado = request.args.get("titulo", "").strip().lower()
    resultado = None

    if titulo_procurado:
        for livro in banco_livros:
            if livro.get_titulo().lower() == titulo_procurado:
                resultado = livro
                break

    return render_template("buscarLivro.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
