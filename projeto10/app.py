from flask import Flask, render_template, request, redirect

app = Flask(__name__)

numero_secreto = None
tentativas = None

@app.route("/", methods=["GET"])
def home():
    global tentativas
    return redirect("/principal")

@app.route("/principal", methods=["GET"])
def principal():
    return render_template("principal.html")

@app.route("/nova_partida", methods=["GET"])
def nova_partida():
    if request.method == "GET":
        global numero_secreto
        global tentativas
        tentativas = 0
        import random
        numero_secreto = random.randint(1, 100)
        return render_template("jogo.html", numero_secreto=numero_secreto)
    
@app.route("/palpite", methods=["POST"])
def palpite():
    if request.method == "POST":
        global numero_secreto
        global tentativas
        tentativas += 1
        palpite = int(request.form['palpite'])

        if palpite < numero_secreto:
            mensagem = "Muito baixo!"
            return render_template('jogo.html', mensagem=mensagem)
        elif palpite > numero_secreto:
            mensagem = "Muito alto!"
            return render_template('jogo.html', mensagem=mensagem)
        else:
            return render_template('acertou.html', tentativas=tentativas)

if __name__ == "__main__":
    app.run(debug=True)
