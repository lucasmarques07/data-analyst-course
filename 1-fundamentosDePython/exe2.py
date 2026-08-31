import pprint

pp = pprint.PrettyPrinter(depth=4)

carrinho = []

soma = 0

produtos = {
    "arroz": 25,
    "feijao": 9,
    "macarrao": 6,
    "leite": 5,
    "cafe": 18,
    "ovo": 22
}

while True:

    print("==============================")
    print("PRODUTO   | PREÇO   ")
    print("------------------------------")
    print("Arroz     | R$ 25,00")
    print("Feijão    | R$  9,00")
    print("Macarrão  | R$  6,00")
    print("Leite     | R$  5,00")
    print("Café      | R$ 18,00")
    print("Ovo       | R$ 22,00")
    print("Fim                ")
    print("==============================")

    opt = input("Escolha uma opção: ").lower()
    
    if opt in produtos:
        
        qtd = int(input('Qual a quantidade? '))

        preco = produtos[opt]
        
        dados_produto = {
            "produto": opt,
            "quantidade": qtd,
            "valor": preco
        }
        
        carrinho.append(dados_produto)
    
    elif opt == 'fim':
        break

    else: 
        print('Produto inválido!')

print('='*6, 'CUPOM','='*6)

for i in carrinho:

    produto = i["produto"]
    preco = i["valor"]
    qtd = i["quantidade"]

    soma += qtd * preco

    print(f'\n{produto.title()}\n')
    print(f'{qtd} X {preco} = {qtd * preco}')

    print('-'*19)

desconto = 0

print(f'\nSubtotal: R${soma}')

if soma > 100:
    desconto = soma * 0.1

elif soma > 200:
    desconto = soma * 0.15

elif soma > 500:
    desconto = soma * 0.2

print(f'\nDesconto: R${desconto}')

print(f'\nTotal: R${soma - desconto}\n')

print('='*6, 'FIM','='*6)