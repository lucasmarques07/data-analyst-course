# ao quadrado de um numero 

from functools import reduce


power = lambda x: x**2

# verifica se é par

isEven = lambda x: x % 2 == 0

# divide um numero por outro 

div = lambda x, y: x/y

# inverte uma string 

reverse = lambda x: x[::-1]


print(power(5))
print(isEven(5))
print(div(5, 2))
print(reverse("Lucas").title())
print(reverse("Iago").title())



movies_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 9.8, 8.0],
    "Incetion": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.0],
    "The Matrix": [8.8, 9.2, 8.5],
}

# media das notas dos filmes
avgRating = lambda movie: sum(ratings[movie]) / len(ratings[movie])

print(f'média de notas: {avgRating("The Matrix")}')

# Função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list

# Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {avgRating(movie_name)}"

print(f"Média de Avaliação do filme The Matrix: {avgRating('The Matrix')}")
print(f"Inception está na lista? {check_movie('Inception')}")
print(f"{recommend_movie('Titanic')}")

# A função map() aplica a mesma operação (definida pela lambda) a todos os itens de uma lista.

numeros = [1, 2, 3, 4]
# Eleva todos os números ao quadrado
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)  # Resultado: [1, 4, 9, 16]

# A função filter() usa uma lambda que retorna True ou False. Ela mantém na lista apenas os elementos que retornarem True.

idades = [12, 18, 25, 40, 15]
# Filtra apenas os maiores de idade
maiores = list(filter(lambda x: x >= 18, idades))

print(maiores)  # Resultado: [18, 25, 40]

# sorted() ou .sort() — Ordenação personalizada Muito útil para ordenar dicionários, tuplas ou objetos complexos com base em uma chave específica.

usuarios = [
    {"nome": "Ana", "idade": 30},
    {"nome": "Carlos", "idade": 22},
    {"nome": "Beto", "idade": 28}
]

# Ordena a lista de dicionários pela chave 'idade'
usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario["idade"])

print(usuarios_ordenados)
# Resultado: Carlos (22), Beto (28), Ana (30)

# reduce() Fica dentro do módulo functools. Ela aplica a lambda cumulativamente aos itens de uma lista, reduzindo-a a um único valor (como uma soma ou multiplicação total).

numeros = [1, 2, 3, 4]
# Multiplica todos os números entre si: ((1 * 2) * 3) * 4
produto = reduce(lambda x, y: x * y, numeros)

print(produto)  # Resultado: 24