#Calculadora de Estatísticas Simples
#Projeto inciante para aprender Python e manipulação de dados.
#Autora: Bianca Vitória de Campos

import os

css_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    text-align: center;
}
.container {
    background-color: #fff;
    padding: 30px;
    margin: 50px auto;
    width: 400px;
    border-radius: 10px;
    box-shadow: 0 0 10px #aaa;
}
h1 { color: #333; }
p { font-size: 18px; }
"""

with open("static/style.css", "w") as f:
    f.write(css_content)

numeros = input("Digite os números separados por vírgula: ")
lista_num = [float(num.strip()) for num in numeros.split(",")]

soma = sum(lista_num)
media = soma / len(lista_num)
maior = max(lista_num)
menor = min(lista_num)
acima_media = [num for num in lista_num if num > media]
perc_acima = len(acima_media) / len(lista_num) * 100

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Calculadora de Estatísticas</title>
    <link rel="stylesheet" href="../static/style.css">
</head>
<body>
    <div class="container">
        <h1>Calculadora de Estat&iacute;sticas</h1>
        <p>Soma: {soma}</p>
        <p>M&eacute;dia: {media}</p>
        <p>Maior valor: {maior}</p>
        <p>Menor valor: {menor}</p>
        <p>Percentual acima da m&eacute;dia: {perc_acima:.2f}%</p>
    </div>
</body>
</html>
"""

html_file = "templates/resultado.html"
with open(html_file, "w") as f:
    f.write(html_content)

print(f"Arquivo HTML gerado: {html_file}")
print("Abra no navegador para ver o resultado.")