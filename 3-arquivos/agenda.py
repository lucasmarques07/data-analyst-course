import os

def addContact():
    name = input("Nome do contato: \n")
    address = input("Endereço do contato: \n")
    phone = input("Telefone do contato: \n")

    contact = f"Nome: {name} \nEndereço: {address} \nTelefone: {phone}"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def viewContacts():
    if not os.path.exists("dados/contatos.txt"):
        print("\nA lista de contatos está vazia!")
        return
    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("\nLista de Contatos: ")
    print(f'{contacts}')

def deleteContact():
    if not os.path.exists("dados/contatos.txt"):
        print("A lista de contatos está vazia!")
        return
    with open("dados/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")