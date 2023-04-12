import random
import time

def buscaVazio(m):
    for l in range(0,3):
        for c in range(0,3):
            if m[l*3+c] == 0:
                return l, c

def buscaEstados(m, l, c):
    abertos = []
    if l < 2:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[(l+1)*3+c] = novoMovimento[(l+1)*3+c], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Baixo"))
    if c < 2:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[l*3+(c+1)] = novoMovimento[l*3+(c+1)], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Direita"))
    if l > 0:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[(l-1)*3+c] = novoMovimento[(l-1)*3+c], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Cima"))
    if c > 0:
        novoMovimento = m.copy()
        novoMovimento[l*3+c], novoMovimento[l*3+(c-1)] = novoMovimento[l*3+(c-1)], novoMovimento[l*3+c]
        abertos.append((novoMovimento, "Esquerda"))
    return abertos


def buscaLargura(abertos, visitados):
    tempoInicio = time.time()
    i = 0
    while abertos:
        estado, acoes = abertos.pop(0)
        i+=1
        visitados.append(estado)
        l, c = buscaVazio(estado)
        a = buscaEstados(estado, l, c)
        for elemento, acao in a:
            if elemento not in visitados:
                if elemento == obj:
                    tempoFim = time.time()
                    tempo = tempoFim - tempoInicio
                    print("\nObjetivo alcançado em",i, "tentativas com um tempo de", tempo, "segundos")
                    print("Caminho de ações executadas:")
                    while acoes:
                        print(acoes.pop(0))
                    print("Estado final: ",elemento)

                    return i, tempo
                abertos.append((elemento, acoes + [acao]))


def solutionLargura(x):
    estadoAtual = x.copy()

    visitados = []
    abertos = [(estadoAtual, [])]

    return buscaLargura(abertos, visitados)

obj = [1, 2, 3, 4, 5, 6, 7, 8, 0]