"""
# ex1
numeros = [3, 7, 10, 15, 20, 21, 30]

pt1 = [n**2 for n in numeros]
print(pt1)

pt2 = [n for n in numeros if n % 10 == 0]
print(pt2)

pt3 = [n + 1 for n in numeros]
print(pt3)

pt4 = [n for n in numeros if n % 2 != 0]
print(pt4)

# ex2
filmes = [
    "Titanic",
    "Alien",
    "Rango",
    "The Batman",
    "La La Land",
    "Wall-E"
]

pt1 = [n for n in filmes if len(n) > 6]
print(pt1)

pt2 = [n for n in filmes if "e" in n.lower()]
print(pt2)

pt3 = [n.upper() for n in filmes]
print(pt3)

pt4 = [len(n) for n in filmes]
print(pt4)

#ex3

def par(n):
    
    return n % 2 == 0
    
print(par(2))

def maior(x, y):
    
    if x > y:
        return x

    return y


print(maior(99,4))

def palindromo(n):

    n = n.lower()
    
    if n == n[::-1]:
        return True
    
    else:
        return False
    
print(palindromo("Radar"))

# ex4

def stats(*n):
    
    sum = 0
    qtd = 0
    maior = None
    menor = None

    for x in n:
        
        sum += x
        qtd += 1

        if maior is None and menor is None:
            maior = x
            menor = x
    
        else: 
            if x > maior:
                maior = x

            if x < menor:
                menor = x

    print(f"O maior é: {maior}")
    print(f"O menor é: {menor}")
    print(f"A quantidade é: {qtd}")
    print(f"A soma é: {sum}")
    print(f"A média é: {sum / len(n)}")

stats(4,8,9,12,1,5)



# ex5

def cadastro(**n):
    for key, value in n.items():
        print(f"{key}: {value}")

cadastro(
    nome="Lucas",
    idade=20,
    cidade="Brasília",
    curso="ADS"
)



# ex6

positivo = lambda x: x > 0

print(positivo(1))

cubo = lambda x: x**3

print(cubo(3))

menor = lambda x, y: x if x < y else y

print(menor(9, 5))

letras = lambda x: len(x)

print(letras("Lucas"))

letraA = lambda n: n[0].lower() == "a"

print(letraA("Amigo"))

"""