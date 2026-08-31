def welcome():
    print('Welcome baby')

def completeName(nome, sobrenome):
    print(f'O seu nome completo é {nome} {sobrenome}')

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')

completeName(nome, sobrenome)

def address(country="Brasil"):
    print(f"Eu moro em: {country}")

address()
address("Portugal")