import numpy as np
import Dessin as d
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import random
import math


def graphe(n: int,p:int) -> np.matrix:
    """
    Génère une matrice de taille n remplie de 50% de 0 et 50% de 1
    :param n: taille de la matrice (n x n)
    :param p: pourcentage de fleches (de 1)
    :return: matrice numpy
    """

    matrixFull = np.zeros((n,n))
    c=0
    while c < n**2*(100-(p*100))//100:
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        if matrixFull[i][j] != 1:
            matrixFull[i][j] = 1
            c += 1
    return matrixFull
def Trans2(M):
    """
    Rernvoie la matrice de fermeture transitive selon l'algorithme Roy-Warshall
    :param M: Matrice non penderee
    :return:Matrice de fermeture transitive
    """
    k = len(M)
    for s in range(k):
        for r in range(k):
            if M[r, s] == 1:
                for t in range(k):
                    if M[s, t] == 1:
                        M[r, t] = 1
    return (M)

def FC(M):
    """
    Rencoie si la matrice est fortement connexe ou non
    :param M: Matrice non ponderee
    :return: True si la matrice est fortement connexe False sinon
    """
    if 0.0 in Trans2(M):
        return False
    else:
        return True

def testStatFC(n):
    """
    Le pourcentage de graphes de taille n fortement connexes pour un test portant sur quelques centaines de graphes.
    :param n: taille n du graphe
    :return: le % de graphe fortement connexe
    """
    r=0
    for i in range(400):
        if FC(graphe(n,0.5)) :
            r += 1
    return (r/400) * 100

def testStatFC2(n,p):
    """
    Le pourcentage de graphes de taille n fortement connexes pour un test portant sur quelques centaines de graphes.
    :param n: taille n du graphe
    :param p: pourcentage de 1 dans la matrice
    :return: le % de graphe fortement connexe
    """
    r = 0
    for i in range(300):
        if FC(graphe(n, p)):
            r += 1
    return (r * 100 / 300)


def seuil(n):
    """
    Renvoie le seuile necessaire pour atteindre 99% de chances d'obtenir un graph fortement convexe
    :param n: taille de la matrice
    :return: % de fleches minimum pour atteindre 99% de chances d'obtenir un graph fortement convexe
    """
    p = 100
    while testStatFC2(n, p / 100) < 99 or p == 0:
        p -= 1
    return p


def graphStatFC():
    x = []
    y = []
    done = False
    for size in tqdm(range(1, 25)):
        x.append(size)
        y.append(testStatFC(size))

        # afficher le chiffre ou % de connexe > 99%
        if y[-1] > 99.0 and done == False:
            plt.text(x[-1], y[-1], size)
            done = True
        # print(size,testStatFC(size))

    plt.plot(x, y)
    plt.grid()
    plt.axhline(y=99, color='r')
    plt.xlabel('Taille de la matrice')
    plt.ylabel('% de forte connexite sur 400 matrices')
    plt.show()


# graphStatFC()
def suiteSeuil():

    x = []
    y = []
    for size in tqdm(range(10, 40)):
        x.append(size)
        y.append(seuil(size))
    plt.plot(x,y)
    for x in x:
        plt.plot(x,y[0]+x, color='red')
        plt.plot(x,math.pow(x,2),color='green')
    plt.legend(['% fleches 99% de forte connexité','fonction affine', 'fonction puissance'])
    plt.xlabel('Taille de la matrice')
    plt.ylabel('seuil de forte connexité')
    plt.show()


suiteSeuil()
