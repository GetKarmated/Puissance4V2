from Plateau import Plateau
from IA import iaJouerJeton
import sys

#classe décrivant un joueur, caractérisé par le fait qu'il soit IA ou non et s'il commence ou non, par défaut le joueur et humain et ne commence pas (jeton jaune)
class Player:
    def __init__(self,start=False, ia=False):
        self.ia=ia
        if start:
            self.couleur='rouge' #les rouges sont les premiers à commencer
        else:
            self.couleur='jaune'
    
    #méthode faisant le processus d'un tour du jeu pour un joueur ou pour l'IA
    def jouer(self, plateau: Plateau):

      #tour pour un joueur
        if not self.ia:
            print("Il reste {} jetons\nJoueur {}, entrez la colonne dans laquelle vous souhaitez jouer (1-12): ".format(plateau.nombreJetons(), self.couleur.upper()), end="")
            
            #entrée de la colonne ou l'on souhaite jouer, avec vérification que l'input soit bien un int entre 1 et 12, demande de réentrer tant que l'input ne respecte pas les conditions
            while True:
                try:
                    colonne= int(input())-1
                    while (colonne<0 or colonne>11 or plateau.matrice[5][colonne].couleur !="blanc") and colonne!=554:
                        print("Colonne invalide, merci de choisir une colonne entre 1 et 12 et non pleine: ")
                        colonne= int(input())-1
                    break
                except:
                    print("Merci de choisir un nombre entre 1 et 12: ", end="")

            #fin de l'exec du prgm
            if colonne==554:
              sys.exit()
            #ajout du jeton dans la colonne choisie 
            plateau.jouerJeton(colonne, self.couleur)
            #affichage du plateau
            print(plateau)

        #tour pour l'IA
        else:
            print("L'IA joue...\n", end="")
            #coup de l'IA
            iaJouerJeton(plateau, self.couleur)
            print(plateau)
