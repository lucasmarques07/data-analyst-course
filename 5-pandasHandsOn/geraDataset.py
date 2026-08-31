import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pastaDataset = Path(__file__).parent / "datasets"

pastaDataset.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {"estado": "SP", "cidade": "São Paulo",
    "vendedores":["Ana Oliveira", "Lucas Pereira"]},
    {"estado": "MG", "cidade": "Belo Horizonte",
    "vendedores":["Carlos Silva", "Fernanda Costa"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro",
    "vendedores":["Juliana Almeida", "Pedro Souza"]},
    {"estado": "RS", "cidade": "Porto Alegre",
    "vendedores":["Mariana Gomes", "Roberto Ferreira"]},
    {"estado": "SC", "cidade": "Florianópolis",
    "vendedores":["Gabriela Santos", "Tiago Lima"]},
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy", "id": 0, "preco": 2500},
    {"nome": "Notebook Dell Inspiron", "id": 1, "preco": 4500},
    {"nome": "Tablet Apple Ipad", "id": 2, "preco": 3000},
    {"nome": "Smartwatch Garmin", "id": 3, "preco": 1200},
    {"nome": "Fone de Ouvido Sony", "id": 4, "preco": 600},
]

FORMA_PAGTO = ["cartão de crédito", "boleto", "pix", "dinheiro"]
GENERO_CLIENTES = ["male", "female"]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    horaCompra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)

    )

    generoCliente = random.choice(GENERO_CLIENTES)
    nomeCliente = names.get_full_name(generoCliente)
    formaPagamento = random.choice(FORMA_PAGTO)

    compras.append({
        "data": horaCompra,
        "id_compra": 0,
        "loja": loja["cidade"],
        "vendedor": vendedor,
        "produto": produto["nome"],
        "cliente_nome": nomeCliente,
        "cliente_genero": generoCliente.replace("female", "feminino").replace("male", "masculino"),
        "forma_pagamento": formaPagamento
    })

dfCompras = pd.DataFrame(compras).set_index("data").sort_index()
dfCompras["id_compra"] = [i for i in range(len(dfCompras))]

dfLojas = pd.DataFrame(LOJAS)
dfProdutos = pd.DataFrame(PRODUTOS)

#Exportando os arquivos
        


dfCompras.to_excel(pastaDataset / "compras.xlsx")
dfLojas.to_excel(pastaDataset / "lojas.xlsx")
dfProdutos.to_excel(pastaDataset / "produtos.xlsx")
