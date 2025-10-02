import re
import requests
from datetime import datetime

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

def get_result(url: str, params: dict):
    result = requests.get(url, params=params).json()

    cadernos = result["items"]

    lista_documentos = []

    for caderno in cadernos:
        documentos = caderno["documents"]
        for documento in documentos:
            lista_documentos.append(documento)

    filtrada = list(filter(filtrar, lista_documentos))

    resultados = []

    for resp in filtrada:
        data_publicacao = resp["dataPublicacao"]
        search = re.search("(\\d{4}-\\d{2}-\\d{2})", data_publicacao)
        if search:
            data_publicacao = datetime.strptime(search.group(1), "%Y-%m-%d").strftime("%d/%m/%Y")
        link_relatorio = "https://dje.tjmt.jus.br/dje/relatorio/" + resp["enderecoCaderno"]

        resultados.append({
            "data_publicacao": data_publicacao,
            "link_relatorio": link_relatorio
        })

    return resultados
