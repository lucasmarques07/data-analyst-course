import numpy as np

mapa = np.random.randint(1,10, size=(5,5))

print(mapa)

#posiciona o tesouro em uma posição aleatória 
while True:
    tesouroLinha, tesouroColuna = np.random.randint(0,5,size=(2))
    if(tesouroLinha, tesouroColuna) != (0,0):
        break

posicaoJogador = (0,0)
pontuacao = 0

def mostrarMapa(mapa, posicaoJogador):
    mapaComJogador = mapa.copy()
    linha, coluna = posicaoJogador
    mapaComJogador[linha, coluna] = -1

    mapaComJogadorStr = np.char.mod('%2d', mapaComJogador) #converte a matriz para string
    mapaComJogadorStr[mapaComJogador == '-1'] = 'P'

    print("\nMapa Atual: ")
    for linha in mapaComJogadorStr:
        print(' '.join(linha))

#Fluxo Principal
while True:
    mostrarMapa(mapa, posicaoJogador)

    direcao = input("Qual direção que deseja mover? (cima, baixo, esquerda, direita)").strip().lower()

    movimentos = {
        "cima":(-1,0),
        "baixo":(1,0),
        "esquerda":(0,-1),
        "direita":(0,1),
        "c":(-1,0),
        "b":(1,0),
        "e":(0,-1),
        "d":(0,1)
    }

    if direcao in movimentos:
        novaPosicao = (posicaoJogador[0] + movimentos[direcao][0], 
                       posicaoJogador[1] +  movimentos[direcao][1])
    else:
        print("Posição inválida. Tente novamente!")

    if not (0 <= novaPosicao[0] < mapa.shape[0] and 0 <= novaPosicao[1] < mapa.shape[1]):
        print("Movimento fora dos limites. Tente novamente")
        continue

    posicaoJogador = novaPosicao
    pontuacao += 1

    if posicaoJogador == (tesouroLinha, tesouroColuna):
        linha = int(tesouroLinha)
        coluna = int(tesouroColuna)
        mostrarMapa(mapa, posicaoJogador)
        print("=====Parabéns! Você encontrou o tesouro!=====")
        print(f"Pontuação final: {pontuacao}")
        print(f"O tesouro estava na posição: {linha, coluna}")
        break