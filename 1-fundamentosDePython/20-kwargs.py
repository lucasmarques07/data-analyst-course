"""

*args usados quando não se sabe ao certo o número de argumnetos que precisam ser passados em uma função
eles vão ser passados por meio de uma tupla
**kwargs usados para passar chaves e valores como argumentos
eles vão ser passados por meio de um dicionario

"""

# soma de numeros

def sum(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(f'A soma total é: {sumTotal}')

print(sum(1,2,3,4,5,6,7,8,9,10))

def times(**equipes):
    for key, value in equipes.items():
        print(f"{key} - {value}")

print("Lista de times:")

times(TIME="Palmeiras", BRASILEIROES=12)
times(TIME="Flamengo", BRASILEIROES=8)
times(TIME="Santos", BRASILEIROES=8)