import random
import time

def buscaVazio(m):
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []
    if l < 2:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l+1][c] = novoMovimento[l+1][c], 0
        abertos.append((novoMovimento, "Baixo", heuristicaDistancia(novoMovimento, obj) ))
    if c < 2:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l][c+1] = novoMovimento[l][c+1], 0
        abertos.append((novoMovimento, "Direita", heuristicaDistancia(novoMovimento, obj)))
    if l > 0:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l-1][c] = novoMovimento[l-1][c], 0
        abertos.append((novoMovimento, "Cima", heuristicaDistancia(novoMovimento, obj)))
    if c > 0:
        novoMovimento = [list(l) for l in m]
        novoMovimento[l][c], novoMovimento[l][c-1] = novoMovimento[l][c-1], 0
        abertos.append((novoMovimento, "Esquerda", heuristicaDistancia(novoMovimento, obj)))
    return abertos

def heuristicaDistancia(estadoAtual, obj):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estadoAtual[i][j]
            if valor != 0:
                linhaObj, colunaObj = buscaPosicao(obj, valor)
                distancia += abs(i - linhaObj) + abs(j - colunaObj)
    return distancia

def buscaPosicao(m, valor):
    for l in range(3):
        for c in range(3):
            if m[l][c] == valor:
                return l, c

def calculaPenalidade(m, obj):
    penalidade = 0
    custo = 1
    for l in range(0,3):
        for c in range(0,3):
            if m[l][c] != 0 and m[l][c] != obj[l][c]:
                if l > 0 and m[l-1][c] == obj[l][c] and m[l][c] == obj[l-1][c]:
                    penalidade +=custo
                elif l < 2 and m[l+1][c] == obj[l][c] and m[l][c] == obj[l+1][c]:
                    penalidade +=custo
                if c > 0 and m[l][c-1] == obj[l][c] and m[l][c] == obj[l][c-1]:
                    penalidade +=custo
                elif c < 2 and m[l][c+1] == obj[l][c] and m[l][c] == obj[l][c+1]:
                    penalidade +=custo
    return penalidade

def buscaAEstrela():
    tempoInico = time.time()
    i = 0
    while abertos:
        estado, acoes, custo = abertos.pop(0)
        i += 1
        visitados.append(estado)
        l, c = buscaVazio(estado)
        a = buscaEstados(estado, l, c)
        for elemento, acao, custo in a:
            if elemento not in visitados:
                if elemento == obj:
                    tempoFim = time.time()
                    print("\nObjetivo alcançado em", i, "tentativas com um tempo de", tempoFim - tempoInico, "segundos")
                    print("Caminho de ações executadas:")
                    while acoes:
                        print(acoes.pop(0))
                    print("Estado final: ", elemento)
                    return
                custoReal = len(acoes) + 1
                custoEstimado = custo
                custoPenalidade = calculaPenalidade(elemento, obj)
                custoTotal = custoReal + custoEstimado + custoPenalidade
                abertos.append((elemento, acoes + [acao], custoTotal))
        abertos.sort(key=lambda x: x[2])

obj = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print("Meu objetivo é:")
print(obj)

# x = list(range(0,9))
# random.shuffle(x)

# x1 = x[:3]
# x2 = x[3:6]
# x3 = x[6:]

# x = [x1, x2, x3]

# x = [[0, 5, 3], [7, 2, 6], [4, 1, 8]] # 17 acoes
# x = [[6, 7, 5], [1, 2, 3], [0, 4, 8]] # 18 acoes
x = [[3, 1, 8], [5, 6, 2], [7, 4, 0]] # 24 acoes
# x = [[8, 6, 7], [2, 5, 4], [3, 0, 1]] # 31 acoes


# x = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

estadoAtual = x.copy()
print("Matriz de estado inicial é:")
print(estadoAtual)

visitados = []
abertos = [(estadoAtual, [], 0)]

# buscaLargura()
buscaAEstrela()
