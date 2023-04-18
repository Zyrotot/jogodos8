# Algoritmos
## buscaLargura.py
Algoritmo de busca em largura

## buscaAestrela.py
Algoritmo A* usando a distância de Manhattan como Heurística

## buscaHeuristica.py
Algoritmo A* usando a distância de Manhattan como Heurística e aplicando penalidade para peças invertidas

# Comparação

Tabela comparativa com o número de nós visitados por cada método, para tabuleiros com diferentes tamanhos de resposta mínima

|         | buscaLargura | buscaAestrela | buscaHeuristica |
|---------|--------------|---------------|-----------------|
|   18    |      20607   |       169     |           134    |
|   24    |        NA    |      2116     |          1782    |
|   31    |        NA    |     19763     |         18513    |