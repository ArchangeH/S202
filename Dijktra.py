from typing import List, Tuple
import numpy as np
import graphviz as gr
import Dessin
#D3
INF = float("inf")
# petite matrice de test
#M = [
#    [INF, INF, 22, INF],
#    [INF, 16, INF, INF],
#    [INF, 54, INF, 27],
#    [INF, INF, 30, INF],
#]

def Dijkstra(M: List[List[int]], d: int, arrive: int):
    """
    Implémentation python de l'algorithme de Dijkstra
    :param M: Matrice carré à valeur aléatoire
    :param d: sommet de départ
    :param arrive: sommet d'arriver
    :return: Lance la fonction resToList qui transforme nos résultats en liste
    pour faciliter les dessins de graphes et la lecture du chemin
    """
    dist = {d: 0} # Initialisation de l'algorithme
    pred = {d: d}
    v = [d]
    n = len(M)
    for i in range(n): # Pour chaque successeur de d
        if M[d][i] != INF: # si le poid de d vers le succèsseur n'est pas infini
            dist[i] = M[d][i] # ajout des valeurs dans les dictionnaires
            pred[i] = d
        else: # sinon
            dist[i] = INF # ajout de valeur non définie
            pred[i] = None
    mini = INF
    for k, val in dist.items(): # pour chaque elements de dist (k = clé, val = valeur)
        if val < mini: # on cherche le sommet s avec le poid minimum pour y acceder
            s = k
            mini = val
    try: # on essaye le code suivant une première (il est possible de ne pas trouver de sommets s)
        while s not in v: # si s existe et tant qu'il n'est pas dans v
            v.append(s) # on l'ajoute à v et on cherche ses successeurs t
            for t in range(n):
                if t not in v: # si le successeur t n'est pas dans v
                    if dist[s] + M[s][t] < dist[t]: # et que la distance de s + le poid de s → t est inférieur à la distance de t
                        dist[t] = dist[s] + M[s][t] # on met à jour les veleurs et t devient s
                        pred[t] = s
    except UnboundLocalError: # si s n'a pas été trouvé alors il n'y a pas de chemin partant de d
        print(f"Aucune fleche ne part du départ {d}")
        return None
    if pred[arrive] is None: # si l'arrivée n'a pas de predecesseur
        return None # fin du programme
    else:
        return Dessin.restolist(M, dist, pred, d, arrive) # sinon le chemin est envoyé au programme exprimant le chemin


if __name__ == "__main__":
    n = int(input("quelle est la taille de la matrice ? \n"))
    d = int(input(f"quel est le sommet de départ ? (entre 0 et {n - 1})"))
    s = int(input(f"quel est le sommet d'arrivée ? (entre 0 et {n - 1})"))

    M = Dessin.graphe(n, int(input("quelle est la valeur a de l'itervalle [a,b]")),
                      int(input("quelle est la valeur b de l'itervalle [a,b]")))
    # Décommentez ce code pour utiliser les matrice avec p% de flèche (commentez celui du dessus)
    # M = Dessin.graphe2(n, int(input("quelle est la proportion p de fleche ? (entre 0 et 1) \n")),
    #                       int(input("quelle est la valeur a de l'itervalle [a,b] ? \n")),
    #                       int(input("quelle est la valeur b de l'itervalle [a,b] ? \n")))

    c = Dijkstra(M, d, s)
    if c is None:
        print("Aucun chemin n'a été trouvé")
    else:
        print("Existence d'un chemin")
        Dessin.redpath(Dessin.matToGraphe(M), c).render(format="png", view=True)
        # pensez à regarder si vous n'avez pas une image ouverte si le graphe ne s'affiche pas à l'ecran
        print(c)



