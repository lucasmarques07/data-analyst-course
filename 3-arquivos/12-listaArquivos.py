import glob, os, zipfile

# 1 - diretório de trabalho atual

print(os.getcwd())

# 2 - listar todos os arquivos txt

for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - listar todos os arquivos csv

for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - compactar arquivos .txt

with zipfile.ZipFile("dados/names.zip", "w") as zip:
    for file in glob.glob("dados/*.txt"):
        zip.write(file)

# 5 - compactar todos os arquivos

with zipfile.ZipFile("code.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)