from Plateau import Plateau
from Jeton import Jeton
import time

# Décalage à appliquer en abscisse pour chaque direction
DIRECTION_DELTA_X = [1, 0, 1, 1]
# Décalage à appliquer en ordonnée pour chaque direction
DIRECTION_DELTA_Y = [0, 1, 1, -1]

def minimax_alpha_beta(plateau: Plateau, couleur: str, couleurIA: str, depth: int, maximizingPlayer: bool, alpha: float, beta: float):
                plateau_test = Plateau(historique= plateau.historique.copy())
                # Vérifie si on est arrivé à la profondeur maximale ou si le jeu est terminé
                try:
                    state= plateau_test.state(plateau_test.historique[-1])
                except:
                    state= plateau_test.state(None)

                if depth == 0 or state== 2 or state == 1:
                    return None, heuristicValue(plateau_test, couleurIA)

                # Maximizing player
                if maximizingPlayer:
                    value = -float("inf")
                    bestColonne= None

                    for colonne in coupsPossibles(plateau_test):
                        ligne= plateau_test.jouerJeton(colonne, couleur)
                        plateau_test.jouerJeton(colonne, couleur)
                        new_value = minimax_alpha_beta(plateau_test, getCouleurAdverse(couleur), couleurIA, depth-1, False, alpha, beta)[1]
                        if new_value > value:
                            value = new_value
                            bestColonne= colonne
                            bestLigne= ligne
                        alpha = max(alpha, value)
                        if beta <= value:
                            break  # élagage Alpha-Beta
                    return (bestLigne, bestColonne), value

                # Minimizing player
                else:
                    value = float("inf")
                    bestColonne = None

                    for colonne in coupsPossibles(plateau_test):
                        ligne= plateau_test.jouerJeton (colonne, couleur)
                        plateau_test.jouerJeton(colonne, couleur)
                        new_value = minimax_alpha_beta(plateau_test, getCouleurAdverse(couleur), couleurIA, depth-1, True, alpha, beta)[1]
                        if new_value < value:
                            value = new_value
                            bestColonne = colonne
                            bestLigne= ligne
                        beta = min(beta, value)
                        if value <= alpha:
                            break  # élagage Alpha-Beta
                    return (bestLigne, bestColonne), value

def coupsPossibles(plateau: Plateau):
    coupsPossibles=[]
    for i in range(12):
        if plateau.matrice[5][i]==None:
            coupsPossibles.append(i)
    return coupsPossibles
        
def getCouleurAdverse(couleur: str):
    return 'jaune' if couleur=='rouge' else 'rouge'

def heuristicValue(plateau: Plateau, couleur: str):

    # Les valeurs de l'heuristique pour chaque direction possible
    score = [0] * 4  # [horizontal, vertical, diagonale /, diagonale \]

    # On parcourt toutes les directions possibles
    for direction in range(4):
        # On parcourt toutes les positions sur le plateau dans cette direction
        for i in range(4):
            for j in range(4):
                # On récupère le jeton à cette position
                jeton = plateau.matrice[i][j]
                if jeton != None:
                    break
                else:
                    print("ok")
                # On ne traite que les jetons du joueur actuel
                    if jeton.couleur == couleur:
                        # On initialise le nombre de jetons alignés à 1
                        jetonsAlignes = 1

                        # On parcourt les positions suivantes dans la direction courante
                        for k in range(1, 4):
                            # On calcule les coordonnées de la position suivante
                            x = i + k * DIRECTION_DELTA_X[direction]
                            y = j + k * DIRECTION_DELTA_Y[direction]

                            # Si la position est hors du plateau, on sort de la boucle
                            if x < 0 or x >= 4 or y < 0 or y >= 4:
                                break

                            # On récupère le jeton à cette position
                            jetonSuivant = plateau[x][y]

                            # Si le jeton est du joueur actuel, on incrémente le nombre de jetons alignés
                            if jetonSuivant.couleur == couleur:
                                jetonsAlignes += 1
                            # Sinon, si la position est vide, on sort de la boucle
                            elif jetonSuivant == None:
                                break
                            # Sinon, la position est occupée par l'adversaire, on sort de la boucle
                            else:
                                break

                        # On ajoute la valeur heuristique pour cet alignement de jetons dans cette direction
                        score[direction] += 10 ** jetonsAlignes

    # On calcule la valeur heuristique totale en faisant la somme des valeurs pour toutes les directions
    scoreTotal = sum(score)
    # On retourne la valeur heuristique totale
    return scoreTotal

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
    ligne, colonne= minimax_alpha_beta(plateau, couleur, couleur, 4, -float('inf'), float('inf'), True)[0]
    jeton = Jeton(ligne, colonne, couleur)
    plateau.matrice[ligne][colonne] = jeton
    plateau.historique.append(jeton)
    print("Colonne jouée par l'IA: {}".format(colonne+1))
    return 0
 