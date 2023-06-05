from typing import List, Tuple
import random as r
import numpy as np
import graphviz as gr
import Dessin as d

INF = float("inf")


def flecheRandom(M):
    fleche = []
    n = len(M)
    for x in range(n):
        for y in range(n):
            fleche.append(((x, y), M[x][y]))
    r.shuffle(fleche)
    return fleche


def flechePL(M, s):
    fleche = [s]
    n = len(M)
    mem = {}  # On colorie tous les sommets en blanc et s (départ) en vert
    for i in range(n):
        mem[i] = 1
    mem[s] = 0
    file = [s]
    while file:
        i = file[0]  # on prend le premier terme de la file
        for y in range(n):  # On enfile les successeurs de i encore blancs:
            if M[file[0]][y] != INF and mem[y] == 1:
                file.append(y)
                mem[y] = 0  # On les colorie en vert (sommets visités)
                fleche.append(((file[0], y), M[file[0]][y]))  # On les place dans la liste Resultat
        file.pop(0)  # on défile i (on retire le premier élément)
    return fleche


def flechePP(M, s):
    n = len(M)  # taille du tableau = nombre de sommets
    mem = {}  # On colorie tous les sommets en blanc et s en vert
    for i in range(n):
        mem[i] = 1
    mem[s] = 0
    pile = [s]  # on initialise la pile à s
    fleche = []  # on initialise la liste des résultats à s

    while pile:  # tant que la pile n'est pas vide,
        i = pile[-1]  # on prend le dernier sommet i de la pile
        SuccMem = []  # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if M[i, j] != INF and mem[j] == 1:
                SuccMem.append((i,j))
        if SuccMem:  # s'il y en a,
            v = SuccMem[0][1]  # on prend le premier (si on veut l'ordre alphabétique)
            mem[v] = 0  # on le colorie en vert, 
            pile.append(v)  # on l'empile
            fleche.append(((SuccMem[0][0], v), M[SuccMem[0][0]][v]))  # on le met en liste rsultat
        else:  # sinon:
            pile.pop()  # on sort i de la pile

    return fleche


def BellmanFordRandom(M: List[List[int]], d: int, arrive: int):
    n = len(M)
    dist = {d: 0}
    pred = {d: d}
    for x in range(n):
        if x != d:
            dist[x] = INF

    # fleche = flecheRandom(M)
    fleche = flechePP(M, d)
    print(fleche)
    n = len(M)
    # TODO separer le génration des fleche, generation aleatoire, largeur longueur en liste
    # fleche OK
    modif = True
    nbIter = 0
    while modif == True and nbIter <= n - 1:
        modif = False
        for e in fleche:
            if dist[e[0][0]] + e[1] < dist[e[0][1]]:
                dist[e[0][1]] = dist[e[0][0]] + e[1]
                pred[e[0][1]] = e[0][0]
                modif = True
        nbIter += 1
    if nbIter == n:
        return print("pas de plus court chemin : presence d'un cycle de poids négatif")
    else:
        return restolist(M, dist, pred, d, arrive)


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
    res.insert(0, (d, d, d))
    return res


M = d.graphe(8, 1, 62)
c = BellmanFordRandom(M, 7, 3)
d.redpath(d.matToGraphe(M), c).render(format="png", view=True)
