import pandas as pd
import os
from pathlib import Path

# 1 - importando os dados de todas as sheets
tb_clientes_dict = pd.read_excel("dados/clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)
print(type(tb_clientes_dict))

# 2 - criando a pasta 'planilhas_separadas' se não existir
pastaCriada = "dados/planilhas_separadas"
if not os.path.exists(pastaCriada):
    os.makedirs(pastaCriada)

# 3 - separar as planilhas
for Nomeaba, tabela in tb_clientes_dict.items():
    caminhoArquivo = os.path.join(pastaCriada, f"{Nomeaba}.xlsx")
    tabela.to_excel(caminhoArquivo, index=False)

# 4 - criando a pasta 'planilhas_separadas' se não existir
pastaConsolidada = "dados/planilhas_consolidadas"
if not os.path.exists(pastaConsolidada):
    os.makedirs(pastaConsolidada)

# 5 - caminho para o arquivo

caminhoArquivoConsolidado = os.path.join(pastaConsolidada, "clientes.xlsx")

# 6 - consolidar planilhas

with pd.ExcelWriter(caminhoArquivoConsolidado) as consolidada:
    for arquivo in Path(pastaCriada).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)