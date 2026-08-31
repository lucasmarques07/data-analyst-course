"""
flamengo = {
    "Nome": "Flamengo",
    "Ano Fundação": 1895,
    "Quantidade de Libertadores" : 4,
    "Melhores Jogadores": ["Paquetá","Jorginha", "Arrascaeta"]
}

print(flamengo)

print(len(flamengo))

print(type(flamengo))

print(flamengo["Melhores Jogadores"])

print(flamengo.get("Nome"))

print(flamengo.keys())

print(flamengo.values())

print(flamengo.items())

flamengo['Mundiais'] = 1

print(flamengo)

flamengo.update({'Nome': 'Mengo'})

print(flamengo)

flamengo.pop('Mundiais')

print(flamengo)
"""

produtos = {}

for n in range(3):
    nome = input('Qual nome do produto: ')
    preco = float(input('Preço: '))
    produtos[nome] = preco


print(produtos)
print(max(produtos, key=produtos.get))
print(round(sum(produtos.values()) / len(produtos), 2))