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

        mini = INF
        for k,val in dist.items():
            if val < mini and k not in v:
                s = k
                mini = val
    if pred[arrive] == None:
        return None
    else:
        return restolist(M, dist, pred, d, arrive)

def restolist(M: List[List[int]], dist, pred, d, a):
    res = [(a, pred[a], dist[a])]
    distance = res[0][2]
    while res[0][1] is not None and res[0][0] != d:
        res.insert(0, (res[0][1], pred[res[0][1]], dist[res[0][1]]))
        distance += res[0][2]

    #print(res[-1][2])
    #print(res[1:])
# TODO if un element dan res -> element supprimé
# index error
    if len(res) != 1:
        res = res[::-1][:-1]
    for i in range(len(res)):
        res[i] = (res[i][0], res[i][1], M[res[i][1]][res[i][0]])
    res.insert(0, (d, d, d))
    return res

M = d.graphe2(4, 0.3, 1, 62)
#d.matToGraphe(M).render(format="png", view=True)
c = Dijkstra(M, 0, 3)
if c == None:
    print("Aucun chemin n'a été trouvé")
else:
    print("Existence d'un chemin")
    #d.redpath(d.matToGraphe(M), c).render(format="png", view=True)
    pass




