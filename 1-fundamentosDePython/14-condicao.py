# name = input('Nome jogador: \n')
# time = input('Time: \n')
# ucl = int(input('Quantas UCL: \n'))
# mediaGols = float(input('Qual a média de gols: \n'))

# if mediaGols > 0.7 and ucl > 3:
#     print(f'O jogador {name} é muito bom!')
# else: 
#     print(f'O jogador {name} é PÉSSIMO!')

n1 = float(input('Número 1: '))

n2 = float(input('Número 2: '))

op = input('Operação (+ - * /): ')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else: 
    print('INVÁLIDO!')    
    
