import json
import re
import requests
from datetime import datetime

params = {
    "termoDeBusca": "concurso",
    "periodoDataDe": "2025-08-01",
    "indicePagina": 0,
    "quantidadePagina": 10000,
}

url = "https://dje-api.tjmt.jus.br/api/diarioOficial/documentosagrupados"

result = requests.get(url, params=params).json()

cadernos = result["items"]

lista_documentos = []

for caderno in cadernos:
    documentos = caderno["documents"]
    for documento in documentos:
        lista_documentos.append(documento)


filtro = [
    "analista\\s+judici.rio",
    "tecnologia\\s+da\\s+informa..o"
]

def filtrar(data: dict):
    texto = data["documento"]
    resultados = []

    for termo in filtro:
        resultado = re.search(termo, texto, re.IGNORECASE)
        resultados.append(resultado)

    return all(resultados)

filtrada = list(filter(filtrar, lista_documentos))

for resp in filtrada:
    data_publicacao = resp["dataPublicacao"]
    search = re.search("(\\d{4}-\\d{2}-\\d{2})", data_publicacao)
    if search:
        data_publicacao = datetime.strptime(search.group(1), "%Y-%m-%d").strftime("%d/%m/%Y")
    link_relatorio = "https://dje.tjmt.jus.br/dje/relatorio/" + resp["enderecoCaderno"]

    result = {
        "data_publicacao": data_publicacao,
        "link_relatorio": link_relatorio
    }
    
    print(json.dumps(result, indent=4))
