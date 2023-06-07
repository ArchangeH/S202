import matplotlib.pyplot as plt
import Dijktra
import BellmanFord
import Dessin
import time
import matplotlib.pyplot
INF = float("inf")

def tempsDij(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        Dijktra.Dijkstra(M,0,i)
    return time.perf_counter()-t

def tempsBF(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordPP(M,0,i)
    return time.perf_counter()-t

#print(tempsDij(50))
#print(tempsBF(50))
print("test")
for i in range(100):
    print(i)
    plt.scatter(i, tempsDij(200),color='red')
    plt.scatter(i, tempsBF(200),color='blue')


plt.xlabel("N° calcul du temps")
plt.ylabel("Temps pour une matrice de n (s)")
plt.loglog()
plt.show()
