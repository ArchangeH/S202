import matplotlib.pyplot as plt
import Dijktra
import BellmanFord
import Dessin
import time
import matplotlib.pyplot
from tqdm import tqdm
INF = float("inf")
#D3
def tempsDij(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        Dijktra.Dijkstra(M,0,i)
    return time.perf_counter()-t

def tempsBFR(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordR(M,0,i)
    return time.perf_counter()-t

def tempsBFPL(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordPL(M,0,i)
    return time.perf_counter()-t

def tempsBFPP(n:int):
    t = time.perf_counter()
    M = Dessin.graphe(n,0,100)
    for i in range(n):
        BellmanFord.BellmanFordPP(M,0,i)
    return time.perf_counter()-t

for i in tqdm(range(50)):
    plt.scatter(i, tempsDij(i + 4), color='purple')
    plt.scatter(i, tempsBFR(i + 4), color='red')
    plt.scatter(i, tempsBFPL(i + 4), color='blue')
    plt.scatter(i, tempsBFPP(i + 4), color='yellow')

plt.loglog()
plt.legend(['Dijkstra','Belman-Ford Parcours profondeur'])
plt.xlabel("Nombre de sommet de la matrice")
plt.ylabel("Temps pour une matrice de 4 à n+4 sommet")

plt.show()
