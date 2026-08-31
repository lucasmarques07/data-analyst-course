from agenda import addContact, deleteContact, viewContacts

def main():
    while True:
        print("\nAgenda de Contatos")
        print("1 - Adicionar Contato")
        print("2 - Lista de Contatos")
        print("3 - Remover Contatos")
        print("4 - Sair")
        
        opt = int(input("Digite a opção: "))

        if opt == 1:
            addContact()
            print("Contatos adicionado!")
        elif opt == 2:
            viewContacts()
        elif opt == 3:
            deleteContact()
        elif opt == 4:
            break
        else:
            print("Opção inválida!")
            continue

main()