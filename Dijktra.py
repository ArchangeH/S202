from typing import List, Tuple
import numpy as np
import graphviz as gr
import Dessin
INF = float("inf")
M = [
    [INF, INF, 22, INF],
    [INF, 16, INF, INF],
    [INF, 54, INF, 27],
    [INF, INF, 30, INF],
    ]
def Dijkstra(M: List[List[int]], d: int, arrive: int):
    """
    Implémentation python de l'algorithme de Dijkstra
    :param M: Matrice carré à valeur aléatoire
    :param d: sommet de départ
    :param arrive: sommet d'arriver
    :return: Lance la fonction resToList qui transforme nos résultats en liste pour
    faciliter les dessins de graphes et la lecture du chemin
    """
    dist = {d: 0}
    pred = {d: d}
    v = [d]
    n = len(M)

    for i in range(n):
        if M[d][i] != INF:
            dist[i] = M[d][i]
            pred[i] = d
        else:
            dist[i] = INF
            pred[i] = None

    mini = INF
    for k, val in dist.items():
        if val < mini:
            s = k
            mini = val
    try:
        while s not in v:
            v.append(s)
            for t in range(n):
                if t not in v:
                    if dist[s] + M[s][t] < dist[t]:
                        dist[t] = dist[s] + M[s][t]
                        pred[t] = s
    except UnboundLocalError:
        print(f"Aucune fleche ne part du départ {d}")
        return None

    if pred[arrive] is None:
        return None
    else:
        return Dessin.restolist(M, dist, pred, d, arrive)


M = Dessin.graphe2(4, 0.3, 1, 62)
#Dessin.matToGraphe(M).render(format="png", view=True)
c = Dijkstra(M, 0, 3)
if c is None:
    print("Aucun chemin n'a été trouvé")
else:
    print("Existence d'un chemin")
    #Dessin.redpath(Dessin.matToGraphe(M), c).render(format="png", view=True)
    pass




