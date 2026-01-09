#Calculadora de Estatísticas Simples
#Projeto inciante para aprender Python e manipulação de dados.
#Autora: Bianca Vitória de Campos

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numeros = request.form.get("numeros", "")
        lista_num = [float(n.strip()) for n in numeros.split(",") if n.strip()]

        soma = sum(lista_num)
        media = soma / len(lista_num)
        maior = max(lista_num)
        menor = min(lista_num)
        perc_acima = len([n for n in lista_num if n > media]) / len(lista_num) * 100

        return render_template(
            "resultado.html",
            soma=soma,
            media=media,
            maior=maior,
            menor=menor,
            perc_acima=perc_acima
        )

    return render_template("resultado.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
