import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} {self.idade} anos - {self.cidade}"

clientes = [
    Cliente("Ana", 25, "São Paulo"),
    Cliente("Carlos", 30, "Rio de Janeiro"),
    Cliente("Fernanda", 22, "Curitiba")
]

# salvar lista de clientes em arquivo pickle

with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(clientes, f)

# carregando os dados do arquivo pickle

with open("dados/clientes.pkl", "rb") as f:
    clientesCarregados = pickle.load(f)

for c in clientesCarregados:
    print(c)

# Adicionar um novo cliente 
novoCliente = Cliente("Marcos", 28, "Porto Alegre")
clientesCarregados.append(novoCliente)

with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(clientesCarregados, f)

with open("dados/clientes.pkl", "rb") as f:
    clientesCarregados = pickle.load(f)

print(f"\n-------------------\n")

for c in clientesCarregados:
    print(c)