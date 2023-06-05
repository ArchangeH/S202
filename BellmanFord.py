from typing import List, Tuple
import random as r
import numpy as np
import graphviz as gr
import Dessin

INF = float("inf")


def flecheRandom(M):
    """
    Alorgorithme d'ordonnencement des flèches aléatoires
    :param M: La matrice d'adjence à traiter
    :return: Liste non ordonnées de flèche représentant les chemins de la matrice
    """
    fleche = []
    n = len(M)
    for x in range(n):
        for y in range(n):
            fleche.append(((x, y), M[x][y]))
    r.shuffle(fleche)
    return fleche


def flechePL(M, s):
    """
    Algorithme d'ordonnencement des flèches selon le parcours en largeur
    :param M: La matrice d'adjacence à traiter
    :param s: le sommet de départ
    :return: Liste de flèches ordonnées selon un parcours en largeur
    représentant les chemins de la matrice
    """
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
    """
    Algorithme d'ordonnencement des flèches selon le parcours en profondeur
    :param M: La matrice d'adjacence à traiter
    :param s: le sommet de départ
    :return: Liste de flèches ordonnées selon un parcours en profondeur
    représentant les chemins de la matrice
    """
    n = len(M)  # taille du tableau = nombre de sommets
    mem = {}  # On colorie tous les sommets en blanc et s en vert
    for i in range(n):
        mem[i] = 1
    mem[s] = 0
    pile = [s]  # on initialise la pile à s
    fleche = []  # on initialise la liste des résultats à s

    while pile:  # tant que la pile n'est pas vide,
        i = pile[-1]  # on prend le dernier sommet i de la pile
        mem[i] = 0  # on le colorie en vert,
        SuccMem = []  # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if M[i, j] != INF and mem[j] == 1:
                SuccMem.append((i,j))
        if SuccMem:  # s'il y en a,
            v = SuccMem[0][1]  # on prend le premier (si on veut l'ordre alphabétique)
            pile.append(v)  # on l'empile
            for e in SuccMem:
                fleche.append(((e[0], e[1]), M[e[0]][e[1]]))  # on le met en liste rsultat
        else:  # sinon:
            pile.pop()  # on sort i de la pile
    return fleche


def BellmanFordR(M: List[List[int]], d: int, arrive: int):
    """
    Implémentation python de l'algorithme de Bellman Ford
    avec des flèches non ordonnées (aléatoire)
    :param M: Matrice carrée à valeur aléatoire
    :param d: sommet de départ
    :param arrive: sommet d'arrivée
    :return: Lance la fonction resToList qui transforme nos résultats en liste pour
    faciliter les dessins de graphes et la lecture du chemin
    """
    n = len(M)
    dist = {d: 0}
    pred = {d: d}
    for x in range(n):
        if x != d:
            dist[x] = INF
            pred[x] = None
    fleche = flecheRandom(M)
    n = len(M)
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
        print("pas de plus court chemin : presence d'un cycle de poids négatif")
        return None
    elif not fleche:
        print("Aucun chemin n'a ete trouve")
        return None
    else:
        return Dessin.restolist(M, dist, pred, d, arrive)

def BellmanFordPL(M: List[List[int]], d: int, arrive: int):
    """
    Implémentation python de l'algorithme de Bellman Ford
    avec des flèches ordonnées selon un parcour en largeur
    :param M: Matrice carrée à valeur aléatoire
    :param d: sommet de départ
    :param arrive: sommet d'arrivée
    :return: Lance la fonction resToList qui transforme nos résultats en liste pour
    faciliter les dessins de graphes et la lecture du chemin
    """
    n = len(M)
    dist = {d: 0}
    pred = {d: d}
    for x in range(n):
        if x != d:
            dist[x] = INF
            pred[x] = None
    fleche = flechePP(M, d)
    n = len(M)
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
        print("pas de plus court chemin : presence d'un cycle de poids négatif")
        return None
    elif not fleche:
        print("Aucun chemin n'a ete trouve")
        return None
    else:
        return Dessin.restolist(M, dist, pred, d, arrive)

def BellmanFordPP(M: List[List[int]], d: int, arrive: int):
    """
    Implémentation python de l'algorithme de Bellman Ford
    avec des flèches ordonnées selon un parcours en profondeur
    :param M: Matrice carrée à valeur aléatoire
    :param d: sommet de départ
    :param arrive: sommet d'arrivée
    :return: Lance la fonction resToList qui transforme nos résultats en liste pour
    faciliter les dessins de graphes et la lecture du chemin
    """
    n = len(M)
    dist = {d: 0}
    pred = {d: d}
    for x in range(n):
        if x != d:
            dist[x] = INF
            pred[x] = None

    fleche = flechePP(M, d)
    n = len(M)
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
        print("pas de plus court chemin : presence d'un cycle de poids négatif")
        return None
    elif not fleche:
        print("Aucun chemin n'a ete trouve")
        return None
    else:
        return Dessin.restolist(M, dist, pred, d, arrive)





M = Dessin.graphe(8, 1, 62)
c = BellmanFordR(M, 0, 3)


if c is not None:
    print("Existence d'un chemin")
    Dessin.redpath(Dessin.matToGraphe(M), c).render(format="png", view=True)
