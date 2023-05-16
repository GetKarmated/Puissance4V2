from Plateau import Plateau
from Player import Player
import sys

if __name__== '__main__':
    plateau = Plateau()

    # Choix du mode de jeu avec sécurité sur l'input
    while True:
        try:
            modeJeu= int(input("Mode de jeu: 1. Joueur contre joueur, 2. Joueur contre IA\n"))
            while modeJeu!=1 and modeJeu!=2 and modeJeu!=555:
                print("Merci de choisir un mode de jeu valide: ")
                modeJeu= int(input())
            break
        except:
            print("Merci de choisir entre 1 et 2: ")

    #fin de l'exec du prgm
    if modeJeu==555:
      sys.exit()

    elif modeJeu==1: # Joueur contre joueur
        joueur1 = Player(start=True)
        joueur2 = Player()
    
    else: # Joueur contre IA

        # choix du joueur qui commence avec sécurité sur l'input
        while True: 
            try:
                start= int(input("Qui commence: 1. Joueur, 2. IA\n"))
                while start!=1 and start!=2 and start!=555:
                    print("Merci de choisir un chiffre valide: ")
                    modeJeu= int(input())
                break
            except:
                print("Merci de choisir entre 1 et 2: ")
        
        #fin de l'exec du prgm
        if start==555:
          sys.exit()

        if start==1: #joueur 1 humain et 2 IA
            joueur1 = Player(start=True)
            joueur2 = Player(ia=True)
        else: #joueur 1 IA et 2 humain
            joueur1 = Player(start=True, ia=True)
            joueur2 = Player()

    while True: # Boucle de jeu
        joueur1.jouer(plateau)
        if plateau.etat(plateau.historique[-1]) == 2:
            print("Match nul !")
            break
        elif plateau.etat(plateau.historique[-1]) == 1:
            print("Le joueur {} a gagné !".format(joueur1.couleur.upper()))
            break

        joueur2.jouer(plateau)
        if plateau.etat(plateau.historique[-1]) == 1:
            print("Le joueur {} a gagné !".format(joueur2.couleur.upper()))
            break
        elif plateau.etat(plateau.historique[-1]) == 2:
            print("Match nul !")
            break