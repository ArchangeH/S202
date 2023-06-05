import numpy as np
import Dessin as d
import time
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
    if 0 in Trans2(M):
        return False
    else:
        return True

def testStatFC(n):
    """
    Le pourcentage de graphes de taille n fortement connexes pour un test portant sur quelques centaines de graphes.
    :param n: taille n du graphe
    :return: le % de graphe fortement connexe
    """
    n=0
    for i in range(300):
        n+=FC(np.random.randint(2,size=(n,n)))
    return

#TODO graphe % de True en fonction de la taille
#TODO finir statFC

M = np.random.randint(2,size=(4,4))
print(FC(M))