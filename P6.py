import matplotlib.pyplot as plt
import Dijktra
import BellmanFord
import Dessin
import time
import matplotlib.pyplot
from tqdm import tqdm
INF = float("inf")

def perfDij(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        Dijktra.Dijkstra(M,0,i)
    return time.perf_counter()-t

def perfBFR(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordR(M,0,i)
    return time.perf_counter()-t

def perfBFPL(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordPL(M,0,i)
    return time.perf_counter()-t

def perfBFPP(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordPP(M,0,i)
    return time.perf_counter()-t

for i in tqdm(range(200)):
    plt.scatter(i, perfDij(i + 4), color='purple')
    #plt.scatter(i, perfBFR(i + 4), color='red')
    #plt.scatter(i, perfBFPL(i + 4), color='blue')
    plt.scatter(i, perfBFPP(i + 4), color='yellow')

plt.loglog()
plt.legend(['Dijkstra','Belman-Ford Parcours profondeur'])
plt.xlabel("Nombre de sommet de la matrice")
plt.ylabel("Temps pour une matrice de 4 à n+4 sommet")

plt.show()
