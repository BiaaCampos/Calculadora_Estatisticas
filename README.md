# Calculadora de Estatísticas - Python

## Descrição

    Projeto iniciante em Python para aprendizado de manipulação de dados e desenvolvimento web simples com Flask.

    Ela permite ao usuário inserir uma lista de números e gera automaticamente as principais métricas, como:

    Média, Soma, Maior e menor valor e Percentual de valores acima da média

    **É um projeto inicial para quem deseja aprender Python e análise de dados.** 

## Funcionalidades

    Entrada de números pelo usuário

    Cálculo automático de soma, média, maior e menor valores

    Percentual de números acima da média

    Visualização do resultado em uma página web amigável

    Estilo simples via CSS

    ## Tecnologias usadas

    Python 3.x

    Flask (para criar a aplicação web)

    HTML/CSS (para interface)

## Como usar

    Clone o repositório:

    git clone https://github.com/seu-usuario/Calculadora-Estatisticas.git


    Entre na pasta do projeto:

    cd calculadora-estatisticas

    Instale o Flask

    python -m pip install flask

    Execute o servidor Flask:

    python app.py

    Abra o navegador e acesse:

    http://127.0.0.1:8000

## Como funciona?

    1. Digite os números separados por vírgula no formulário da página.
    2. clique em **Calcular**
    3. O resultado será exibido logo abaixo do formulário: soma, média, maior e menor valor, e percentual acima da média.

## Exemplo de execução

    Digite os valores separados por vírgula: 5,8,7,6,9
    Média: 7.0
    Soma: 35
    Maior valor: 9
    Menor valor: 5
    Valores acima da média: 40%

## Estrutura do projeto

 calculadora_estatistica/
│
├── app.py                 
├── templates/
│   └── resultado.html     
├── static/
│   └── style.css         
└── README.md 

## OBSERVAÇÕES 

 Este projeto é voltado para iniciantes e aprendizado em Python e Flask.
 A aplicação funciona melhor fora de pastas sincronizadas com o OneDrive (para evitar problemas de permissão).
 A interface pode ser melhorada futuramente com JavaScript para atualizar resultados sem recarregar a página.
