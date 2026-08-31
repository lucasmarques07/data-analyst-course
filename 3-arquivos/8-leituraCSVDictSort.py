import pprint

cursos = []

with open("dados/cursos.csv", "r", encoding='utf-8') as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {"language": linguagem, "category": categoria}
        cursos.append(curso)
    
pp = pprint.PrettyPrinter(depth=4)

pp.pprint(cursos)

def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

for curso in sorted(cursos, key=get_language):
    print(f"{curso["language"]}-{curso["category"]}")
