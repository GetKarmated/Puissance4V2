from Plateau import Plateau
from Jeton import Jeton
import time

def minimax_alpha_beta(plateau: Plateau, couleur: str, couleurIA: str, depth: int, maximizingPlayer: bool, alpha: float, beta: float,depthMax = 5):

    # Vérifie si on est arrivé à la profondeur maximale ou si le jeu est terminé
    try:
        state= plateau.state(plateau.historique[-1])
    except:
        state= plateau.state(None)

    if state == 1:
        scoreFinal = 100000 / (depthMax+1-depth)
        valeur = -scoreFinal if maximizingPlayer else scoreFinal
        # print(valeur)
        # print(plateau)
        return valeur
    if state == 2:
        print("plateau plein")
        return 0
    if depth == 0:
        valeur = heuristicValue(plateau, couleurIA)
        # print(valeur)
        # print(plateau)

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

def coupsPossibles(plateau: Plateau):
    coupsPossibles=[]
    for i in range(12):
        if plateau.matrice[5][i].couleur=="blanc":
            coupsPossibles.append(i)
    return coupsPossibles
        
def getCouleurAdverse(couleur: str):
    return 'jaune' if couleur=='rouge' else 'rouge'

def heuristicValue(plateau: Plateau, couleurIA: str):
    multiplier = [1, 5]
    score = ptsVertical(plateau, couleurIA, multiplier) + \
        ptsHorizontal(plateau, couleurIA, multiplier) + \
        ptsDiagonale(plateau, couleurIA, multiplier)
    return score


def ptsVertical(plateau: Plateau, couleurIA: str, multiplier: int):
    inARow = 0
    threes = 0
    twos = 0
    for i in range(12):
        for j in range(6):
                if plateau.matrice[j][i].couleur == couleurIA:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    threes += 1
                    twos -= 1
                elif inARow == 2:
                    twos += 1
        inARow = 0
    return twos * multiplier[0] + threes * multiplier[1]


def ptsHorizontal(plateau: Plateau, couleurIA: str, multiplier: int):
    inARow = 0
    threes = 0
    twos = 0
    for i in range(6):
        for j in range(12):
                if plateau.matrice[i][j].couleur == couleurIA:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == 3:
                    threes += 1
                    twos -= 1
                elif inARow == 2:
                    twos += 1
        inARow = 0
    return twos * multiplier[0] + threes * multiplier[1]


def ptsDiagonale(plateau: Plateau, couleurIA: str, multiplier: int):
    inARow = [0, 0, 0, 0]
    threes = 0
    twos = 0
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
                        threes += 1
                        twos -= 1
                    elif r == 2:
                        twos += 1
        inARow = [0, 0, 0, 0]

    return twos * multiplier[0] + threes * multiplier[1]

def calculTempsExec(fonction):
    def inner(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print("Temps d'exécution: {} secondes".format(fin - debut))
        return resultat
    return inner

@calculTempsExec
def iaJouerJeton(plateau, couleur: str):
    bestColonne = 0
    bestScore = float("-inf")

    for coup in coupsPossibles(plateau):
        plateau.jouerJeton(coup, couleur)
        score = minimax_alpha_beta(plateau, getCouleurAdverse(couleur), couleur, 5, False,float('-inf'), float('inf'), 5)
        plateau.annulerCoup()
        print("Score: {}, Coups :{}".format(score,coup))
        if score > bestScore:
            bestScore = score
            bestColonne = coup
    plateau.jouerJeton(bestColonne, couleur)
    print("Colonne jouée par l'IA: {}".format(bestColonne+1))
    return 0
 