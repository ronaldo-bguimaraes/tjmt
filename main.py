from src.tjmt import get_result


params = {
    "termoDeBusca": "concurso",
    "periodoDataDe": "2025-08-01",
    "indicePagina": 0,
    "quantidadePagina": 10000,
}

url = "https://dje-api.tjmt.jus.br/api/diarioOficial/documentosagrupados"

print(get_result(url, params))