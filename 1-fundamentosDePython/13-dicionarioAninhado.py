import pprint

times = {
    "flamengo": {
        "Nome": "Clube de Regatas do Flamengo",
        "Ano Fundação": 1895,
        "Quantidade de Libertadores": 3,  # Ajustado para o dado real atualizado
        "Melhores Jogadores": ["Zico", "Gabigol", "Arrascaeta"]
    },
    "palmeiras": {
        "Nome": "Sociedade Esportiva Palmeiras",
        "Ano Fundação": 1914,
        "Quantidade de Libertadores": 3,
        "Melhores Jogadores": ["Ademir da Guia", "Dudu", "Veiga"]
    },
    "sao_paulo": {
        "Nome": "São Paulo Futebol Clube",
        "Ano Fundação": 1930,
        "Quantidade de Libertadores": 3,
        "Melhores Jogadores": ["Rogério Ceni", "Raí", "Kaká"]
    },
    "santos": {
        "Nome": "Santos Futebol Clube",
        "Ano Fundação": 1912,
        "Quantidade de Libertadores": 3,
        "Melhores Jogadores": ["Pelé", "Neymar", "Ganso"]
    }
}

pp = pprint.PrettyPrinter(depth=4)

pp.pprint(times)

print(times["flamengo"]["Nome"])

times["palmeiras"]["Nome"] = "PORCOS SUJOS"

pp.pprint(times)

del times["santos"]

pp.pprint(times)