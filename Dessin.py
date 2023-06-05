import random
from typing import List, Tuple
import numpy as np
import graphviz as gr
#D3

def graphe(n: int,a: int,b: int) -> np.matrix:
    """
    Génère une matrice de taille n remplie de 50% de coefficient
    infini et de coefficient compris dans l'intervalle [a, b]
    :param n: taille de la matrice (n x n)
    :param a: debut de l'intervalle présent dans la matrice
    :param b: fin de l'intervalle présent dans la matrice
    :return: matrice numpy comtenant 50% de nombre infinit et 50 % de nombres compris dans notre intervalle
    """

    lst =[float(i) for i in range(a,b)]
    c = 0
    matrixFull = np.random.choice(lst, (n, n))
    while c < n**2//2:
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        if matrixFull[i][j] != float('inf'):
            matrixFull[i][j] = float('inf')
            c += 1
    return matrixFull
def graphe2(n: int,p: float,a: int,b: int) -> np.matrix:
    """
    Génère une matrice de taille n remplie de p% de coefficient
    infini et de coefficient compris dans l'intervalle [a, b]
    :param n: taille de la matrice (n x n)
    :param p: proportion de coefficient infini dans la matrice
    :param a: debut de l'intervalle présent dans la matrice
    :param b: fin de l'intervalle présent dans la matrice
    :return: matrice numpy comtenant p% de nombre infinit et (100-p)% de nombres compris dans notre intervalle
    """
    lst = [float(i) for i in range(a, b)]
    c = 0
    matrixFull = np.random.choice(lst, (n, n))
    while c < n**2*(100-(p*100))//100:
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        if matrixFull[i][j] != float('inf'):
            matrixFull[i][j] = float('inf')
            c += 1
    return matrixFull

def matToGraphe(M: np.matrix) -> gr.Digraph:
    """
    Convertie une matrice M en un graphe de la bibliothèque graphviz pour l'affichage
    :param M: matrice de numpy
    :return: Un graphe de la bibliothèque graphviz
    """
    dot = gr.Digraph('graphe', strict=True)
    for i in range(len(M)):
        dot.node(f"{i}", f"{i}")

    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != float('inf'):
                dot.edge(f"{i}", f"{j}", label=f"{int(M[i][j])}")
    return dot


def redpath(graphe: gr.Digraph, chemin: List[Tuple[int, int, int]]) -> gr.Digraph:
    """
    Modifie le dessin d'un graphe pour afficher le chemin en paramètre en couleur (rouge)
    :param graphe: Graphe de la bibliothèque graphviz
    :param chemin: Liste de tuples comprenant les informations pour créer un chemin
    exemple : [(sDepart, sArrivé, poids), ...]
    :return: Un graphe de la bibliothèque graphviz avec le chemin en paramètre en couleur
    """

    for e in chemin:
        graphe.node(f"{e[0]}", f"{e[0]}", color="red")

    chemin.pop(0)
    for e in chemin:
        graphe.edge(f"{e[1]}", f"{e[0]}", label=f"{int(e[2])}", color="red")

    return graphe

