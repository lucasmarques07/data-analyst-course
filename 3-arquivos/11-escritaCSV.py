import csv 

linguagem = input("Informe um nome de linguagem de programação:\n")
categoria = input("Informe a sua categoria:\n")

with open("dados/cursos.csv", "a", encoding="utf-8") as file:

    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem, categoria])