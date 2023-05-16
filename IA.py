from Plateau import Plateau
from Jeton import Jeton
import time

###Fonctions relatives à l'IA

#Algo min max avec elagage alpha beta
def minimax_alpha_beta(plateau: Plateau, couleur: str, couleurIA: str, depth: int, maximizingPlayer: bool, alpha: float, beta: float,depthMax = 5):

    # Vérifie si on est arrivé à la profondeur maximale ou si le jeu est terminé
    try:
        etat= plateau.etat(plateau.historique[-1])
    except:
        etat= plateau.etat(None)

    if etat == 1:
        scoreFinal = 100000 / (depthMax+1-depth)
        valeur = -scoreFinal if maximizingPlayer else scoreFinal
        return valeur
    if etat == 2:
        print("plateau plein")
        return 0
    if depth == 0:
        valeur = heuristicScore(plateau, couleurIA)

        return valeur

    # Maximizing player
    if maximizingPlayer:
        value = float("-inf")

        for colonne in coupsPossibles(plateau):
            plateau.jouerJeton(colonne, couleur)
            value = max(value,minimax_alpha_beta(plateau, getCouleurAdverse(couleur), couleurIA, depth-1, False, alpha, beta,depthMax))
            plateau.annulerCoup()
            alpha = max(alpha, value)
            if beta <= value:
                break  # élagage Alpha-Beta
        return value

    # Minimizing player
    else:
        value = float("inf")

        for colonne in coupsPossibles(plateau):
            plateau.jouerJeton (colonne, couleur)
            value = min(value,minimax_alpha_beta(plateau, getCouleurAdverse(couleur), couleurIA, depth-1, True, alpha, beta,depthMax))
            plateau.annulerCoup()
            beta = min(beta, value)
            if value <= alpha:
                break  # élagage Alpha-Beta
        return value

#methode retournant une liste des colonnes ou il est possible de jouer
def coupsPossibles(plateau: Plateau):
    coupsPossibles=[]
    for i in range(12):
        if plateau.matrice[5][i].couleur=="blanc":
            coupsPossibles.append(i)
    return coupsPossibles

#methode retournant la couleur des jetons de l'adversaire
def getCouleurAdverse(couleur: str):
    return 'jaune' if couleur=='rouge' else 'rouge'

#methode calculant l'heuristique
def heuristicScore(plateau: Plateau, couleurIA: str):
    multiplicateur = [1, 5]
    score = ptsVertical(plateau, couleurIA, multiplicateur) + \
        ptsHorizontal(plateau, couleurIA, multiplicateur) + \
        ptsDiagonale(plateau, couleurIA, multiplicateur)
    return score

#generateur de point:
#on compte sur tout le plateau le nombre de groupe de 2 ou 3 jetons alignés, une fois ces nombres trouvés on applique un coef multiplicateur (1 pour les groupes de 2 et 5 pour les grp de 3)

def ptsVertical(plateau: Plateau, couleurIA: str, multiplicateur: int):
    inARow = 0
    trois = 0
    deux = 0
    for i in range(12):
        for j in range(6):
                if plateau.matrice[j][i].couleur == couleurIA:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    trois += 1
                    deux -= 1
                elif inARow == 2:
                    deux += 1
        inARow = 0
    return deux * multiplicateur[0] + trois * multiplicateur[1]

def ptsHorizontal(plateau: Plateau, couleurIA: str, multiplicateur: int):
    inARow = 0
    trois = 0
    deux = 0
    for i in range(6):
        for j in range(12):
                if plateau.matrice[i][j].couleur == couleurIA:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    trois += 1
                    deux -= 1
                elif inARow == 2:
                    deux += 1
        inARow = 0
    return deux * multiplicateur[0] + trois * multiplicateur[1]

def ptsDiagonale(plateau: Plateau, couleurIA: str, multiplicateur: int):
    inARow = [0, 0, 0, 0]
    trois = 0
    deux = 0
    for i in range(5):
        for j in range(6):
                if j+i < 6:
                    if plateau.matrice[j+i][j].couleur == couleurIA:
                        inARow[0] += 1
                    else:
                        inARow[0] = 0
                    if plateau.matrice[j+i][12 - 1 - j].couleur == couleurIA:
                        inARow[2] += 1
                    else:
                        inARow[2] = 0
                if j+i < 12:
                    if plateau.matrice[j][j+i].couleur == couleurIA:
                        inARow[1] += 1
                    else:
                        inARow[1] = 0
                    if plateau.matrice[j][12 - 1 - j-i].couleur == couleurIA:
                        inARow[3] += 1
                    else:
                        inARow[3] = 0
                for r in inARow:
                    if r == 3:
                        trois += 1
                        deux -= 1
                    elif r == 2:
                        deux += 1
        inARow = [0, 0, 0, 0]

    return deux * multiplicateur[0] + trois * multiplicateur[1]

#décorateur calculant le temps d'execution d'une fonction
def calculTempsExec(fonction):
    def inner(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print("Temps d'exécution: {} secondes".format(fin - debut))
        return resultat
    return inner


#méthode executant le processus de jeu de l'IA
@calculTempsExec
def iaJouerJeton(plateau, couleur: str):
    bestColonne = 0
    bestScore = float("-inf")

    #calcul du meilleur coup grace à l'algo min max
    for coup in coupsPossibles(plateau):
        plateau.jouerJeton(coup, couleur)
        #appel de l'algo
        score = minimax_alpha_beta(plateau, getCouleurAdverse(couleur), couleur, 4, False,float('-inf'), float('inf'), 5)
        plateau.annulerCoup()
        if score > bestScore:
            bestScore = score
            bestColonne = coup

    #ajout du jeton de l'IA sur le plateau
    plateau.jouerJeton(bestColonne, couleur)
    print("Colonne jouée par l'IA: {}".format(bestColonne+1))
    return 0
 