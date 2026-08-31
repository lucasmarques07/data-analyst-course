import json

dados = {
    "clientes":[
        {"id": 1, "nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"id": 2, "nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
        {"id": 3, "nome": "Fernanda", "idade": 22, "cidade": "Curitiba"},
        {"id": 4, "nome": "João", "idade": 35, "cidade": "Belo Horizonte"}
    ]
}

caminhoArquivo = "dados/clientes.json"

# 1 - Escrevendo o arquivo
with open(caminhoArquivo, "w", encoding='utf-8') as f:
    json.dump(dados, f, indent=4)

# 2 - Lendo o arquivo

with open(caminhoArquivo, "r", encoding='utf-8') as f:
    dadosLidos = json.load(f)
    print(dadosLidos)

# 3 - Manipulando dados

for cliente in dadosLidos["clientes"]:
    if cliente["nome"] == "Carlos":
        cliente["idade"] = 20

# 4 - Adicionando dados

novoCliente = {"id": 5, "nome": "Samilly", "idade": 28, "cidade":"Florianópolis"}
dadosLidos["clientes"].append(novoCliente)

# 5 - Salvar os dados manipulados no arquvivo

with open(caminhoArquivo, "w", encoding='utf-8') as f:
    json.dump(dadosLidos, f, indent=4)