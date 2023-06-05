from typing import List, Tuple
import numpy as np
import graphviz as gr
import Dessin as d
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
        return restolist(M, dist, pred, d, arrive)

def restolist(M: List[Tuple[int]], dist, pred, d, a):
    """
    La fonction resToList qui transforme nos résultats en liste pour
    faciliter les dessins de graphes et la lecture du chemin
    :param M: La matrice d'adjascence
    :param dist: dictionnaire des distances renvoyé par dijkstra
    :param pred: dictionnaire des predecesseurs renvoyé par dijkstra
    :param d: le sommet de depart
    :param a: le sommet d'arrivée
    :return: Liste de tuple d'entier qui exprime le chemin de la façon suivante :
    [(sommet, predecesseur, poid), ...]
    le chemin est à lire de droite à gauche, sur un chemin de longueur 4 on aurait
    [(fleche 4), (fleche 3), (fleche 2), (fleche 1)] ou chaque fleche est un tuple comme décrit précedemment.
    """
    res = [(a, pred[a], dist[a])]
    distance = res[0][2]
    while res[0][1] is not None and res[0][0] != d:
        res.insert(0, (res[0][1], pred[res[0][1]], dist[res[0][1]]))
        distance += res[0][2]

    if len(res) != 1:
        res = res[::-1][:-1]
    for i in range(len(res)):
        res[i] = (res[i][0], res[i][1], M[res[i][1]][res[i][0]])
    res.insert(0, (d, d, d))
    return res

M = d.graphe2(4, 0.3, 1, 62)
#d.matToGraphe(M).render(format="png", view=True)
c = Dijkstra(M, 0, 3)
if c is None:
    print("Aucun chemin n'a été trouvé")
else:
    print("Existence d'un chemin")
    #d.redpath(d.matToGraphe(M), c).render(format="png", view=True)
    pass




