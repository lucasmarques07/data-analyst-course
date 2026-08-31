import pprint

cursos = []

with open("dados/cursos.csv", "r", encoding='utf-8') as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {"language": linguagem, "category": categoria}
        cursos.append(curso)
    
pp = pprint.PrettyPrinter(depth=4, sort_dicts=False)

pp.pprint(cursos)

for curso in cursos:
    print(f"{curso["language"]}-{curso["category"]}")
