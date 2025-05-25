from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def perimetroTerreno(largura, comprimento):
    return (largura + comprimento) * 2

def areaTerreno(largura, comprimento):
    return largura * comprimento

@app.route("/")
def home():
    return redirect("principal")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/calculoTerreno", methods=["GET", "POST"])
def calculoTerreno():

    if request.method == "POST":
        largura = float(request.form.get("largura"))
        comprimento = float(request.form.get("comprimento"))
        area = areaTerreno(largura=largura, comprimento=comprimento)
        perimetro= perimetroTerreno(largura=largura, comprimento=comprimento)
        # Banco de dados 

        return render_template(
            "calculoTerreno.html",
            largura=largura,
            comprimento=comprimento,
            area=area,
            perimetro=perimetro    
        )

if __name__ == "__main__":
    app.run(debug=True)