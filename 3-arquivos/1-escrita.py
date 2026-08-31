name = input("Digite o nome de um aluno: ")

# implementação 1
#file = open("dados/names.txt", "a", encoding='utf-8')
#file.write(f"{name}\n")
#file.close()

# implementação 2
with open("dados/names.txt", "a", encoding='utf-8') as file:
    file.write(f"{name}\n")