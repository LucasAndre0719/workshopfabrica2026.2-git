from django.shortcuts import render
import requests
from django.http import JsonResponse


def consultar_cep(requests):

    cep = "58043070"

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta=requests.get(url)

    dados=resposta.json()

    return JsonResponse(dados)


def pagina(requests):
    return render (requests,"home.html")