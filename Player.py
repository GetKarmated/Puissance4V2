from Plateau import Plateau
from IA import iaJouerJeton

class Player:
    def __init__(self,start=False, ia=False):
        self.ia=ia
        if start:
            self.couleur='rouge'
        else:
            self.couleur='jaune'
    
    def jouer(self, plateau: Plateau):
        if not self.ia:
            print("Il reste {} jetons\nJoueur {}, entrez la colonne dans laquelle vous souhaitez jouer (1-12): ".format(plateau.nombreJetons(), self.couleur.upper()), end="")
            while True:
                try:
                    colonne= int(input())-1
                    while colonne<0 or colonne>11 or plateau.matrice[5][colonne].couleur !="blanc":
                        print("Colonne invalide, merci de choisir une colonne entre 1 et 12 et non pleine: ", end="")
                        colonne= int(input())-1
                    break
                except:
                    print("Merci de choisir un nombre entre 1 et 12: ", end="")

            plateau.jouerJeton(colonne, self.couleur)
            print(plateau)
        else:
            print("L'IA joue...\n", end="")
            iaJouerJeton(plateau, self.couleur)
            print(plateau)
