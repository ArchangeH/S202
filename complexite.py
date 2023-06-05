import matplotlib.pyplot as plt

import Dijktra
import BellmanFord
import Dessin
import time
import matplotlib.pyplot
INF = float("inf")

def perfDij(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        Dijktra.Dijkstra(M,0,i)
    return time.perf_counter()-t

def perfBF(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordRandom(M,0,i)
    return time.perf_counter()-t

print(perfDij(200))
print(perfBF(200))

for i in range(100):
    plt.scatter(i, perfDij(50),color='red')
    plt.scatter(i, perfBF(50),color='blue')


plt.xlabel("N° calcul du temps")
plt.ylabel("Temps pour une matrice de n (s)")
plt.show()
