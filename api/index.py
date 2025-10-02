from flask import Flask
app = Flask(__name__)

@app.route("/lista_publicacoes")
def hello_world():
    from src.tjmt import get_result
    params = {
        "termoDeBusca": "concurso",
        "periodoDataDe": "2025-08-01",
        "indicePagina": 0,
        "quantidadePagina": 10000,
    }

    url = "https://dje-api.tjmt.jus.br/api/diarioOficial/documentosagrupados"

    return get_result(url, params)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
