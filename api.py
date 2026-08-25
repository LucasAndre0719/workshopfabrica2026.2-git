import requests


pokemon = input("Qual pokemon você quer saber? ")

resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")


dados = resposta.json()

print(dados['name'])
print(dados['weight'])
print(dados['types'][0]['type']['name'])