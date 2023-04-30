from Plateau import Plateau
from Player import Player

if __name__== '__main__':
    plateau = Plateau()
    while True: # Choix du mode de jeu
        try:
            modeJeu= int(input("Mode de jeu: 1. Joueur contre joueur, 2. Joueur contre IA\n"))
            while modeJeu!=1 and modeJeu!=2:
                print("Merci de choisir un mode de jeu valide: ", end="")
                modeJeu= int(input())
            break
        except:
            print("Merci de choisir entre 1 et 2: ", end="")

    if modeJeu==1: # Joueur contre joueur
        joueur1 = Player(start=True)
        joueur2 = Player()
    
    else: # Joueur contre IA
        while True:
            try:
                start= int(input("Qui commence: 1. Joueur, 2. IA\n"))
                while start!=1 and start!=2:
                    print("Merci de choisir un chiffre valide: ", end="")
                    modeJeu= int(input())
                break
            except:
                print("Merci de choisir entre 1 et 2: ", end="")
        if start==1:
            joueur1 = Player(start=True)
            joueur2 = Player(ia=True)
        else:
            joueur1 = Player(start=True, ia=True)
            joueur2 = Player()

    while True: # Boucle de jeu
        joueur1.jouer(plateau)
        if plateau.state(plateau.historique[-1]) == 2:
            print("Match nul !")
            break
        elif plateau.state(plateau.historique[-1]) == 1:
            print("Le joueur {} a gagné !".format(joueur1.couleur.upper()))
            break

        joueur2.jouer(plateau)
        if plateau.state(plateau.historique[-1]) == 1:
            print("Le joueur {} a gagné !".format(joueur2.couleur.upper()))
            break
        elif plateau.state(plateau.historique[-1]) == 2:
            print("Match nul !")
            break