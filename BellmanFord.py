from typing import List, Tuple
import random as r
import numpy as np
import graphviz as gr
import Dessin as d
INF = float("inf")

def flecheRandom(M):
    dist = {d: 0}
    pred = {d: d}
    fleche = []
    n = len(M)
    for x in range(n):
        if x != d:
            dist[x] = INF
        for y in range(n):
            fleche.append(((x,y), M[x][y]))
    r.shuffle(fleche)
    return [dist, pred, fleche]

def BellmanFord(M: List[List[int]], d: int, arrive: int):
    var = flecheRandom(M)
    dist = var[0]
    pred = var[1]
    fleche = var[2]
    n = len(M)
    # TODO separer le génration des fleche, generation aleatoire, largeur longueur en liste
    #fleche OK
    modif = True
    nbIter = 0
    while modif == True and nbIter <= n-1:
        modif=False
        for e in fleche:
            if dist[e[0][0]] + e[1] < dist[e[0][1]]:
                dist[e[0][1]] = dist[e[0][0]] + e[1]
                pred[e[0][1]] = e[0][0]
                modif=True
        nbIter +=1
    if nbIter == n :
        return print("pas de plus court chemin : presence d'un cycle de poids négatif")
    else:
        return restolist(M, dist,pred,d,arrive)


def restolist(M, dist, pred, d, a):
    res = [(a, pred[a], dist[a])]
    distance = res[0][2]
    while res[0][1] is not None and res[0][0] != d:
        res.insert(0, (res[0][1], pred[res[0][1]], dist[res[0][1]]))
        distance += res[0][2]

    if len(res) != 1:
        res = res[::-1][:-1]
    for i in range(len(res)):
        res[i] = (res[i][0], res[i][1], M[res[i][1]][res[i][0]])
    res.insert(0, (d,d,d))
    return res

M = d.graphe2(4, 0.3, 1, 62)
c = BellmanFord(M, 0, 3)
d.redpath(d.matToGraphe(M), c).render(format="png", view=True)