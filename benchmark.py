from buscaLargura import solutionLargura
from buscaAestrela import solutionAestrela
from buscaHeuristica import solutionHeuristica
import sys

if len(sys.argv) > 1:
    moves = int(sys.argv[1])
else:
    moves = 24

estadosIniciais = {17: [[0, 5, 3], [7, 2, 6], [4, 1, 8]],
                   18: [[6, 7, 5], [1, 2, 3], [0, 4, 8]],
                   24: [[3, 1, 8], [5, 6, 2], [7, 4, 0]],
                   31: [[8, 6, 7], [2, 5, 4], [3, 0, 1]]}

print("Meu estado inicial é:")
print(estadosIniciais[moves], "\n")

if moves > 18:
    tentativasLargura, tempoLargura = "NA", "NA"
else:
    tentativasLargura, tempoLargura = solutionLargura(estadosIniciais[moves])
tentativasAestrela, tempoAestrela = solutionAestrela(estadosIniciais[moves])
tentativasHeuristica, tempoHeuristica = solutionHeuristica(estadosIniciais[moves])

print("\n")
print("{:<15} {:<20} {:<20}".format("Algoritmo", "Nós visitados", "Tempo de execução"))
print("{:<15} {:<20} {:<20}".format("-"*15, "-"*20, "-"*20))
print("{:<15} {:<20} {:<20}".format("Largura", tentativasLargura, tempoLargura))
print("{:<15} {:<20} {:<20}".format("A*", tentativasAestrela, tempoAestrela))
print("{:<15} {:<20} {:<20}".format("Heuristica", tentativasHeuristica, tempoHeuristica))
