from Jeton import Jeton
import numpy as np

class Plateau:

    def __init__(self, historique: list = [], nbLignes: int= 6, nbColonnes: int= 12):
        self.matrice= np.full((nbLignes, nbColonnes), Jeton())
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.historique = historique
        if len(historique) > 0:
            for jeton in historique:
                self.matrice[jeton.ligne][jeton.colonne] = jeton
            
    def __str__(self):
        
        plateau_str = '\n'
        for ligne in self.matrice[::-1]:
            plateau_str += '|'
            for element in ligne:
                if element.couleur != "blanc": plateau_str += ('\033[91m' + 'O' + '\033[0m' if element.couleur=='rouge' else '\033[93m' + 'O' + '\033[0m') + '|'
                else : plateau_str += ' |'

            plateau_str += '\n'
        
        plateau_str += '-------------------------\n 1 2 3 4 5 6 7 8 9 10 11 12\n'

        return plateau_str
    
    def jouerJeton(self, colonne: int, couleur: str):
         for ligne in range(6):
            if self.matrice[ligne][colonne].couleur == "blanc":
                jeton = Jeton(ligne, colonne, couleur)
                self.matrice[ligne][colonne] = jeton
                self.historique.append(jeton)
                return ligne
    def annulerCoup(self):
        if len(self.historique) > 0:
            jeton = self.historique.pop()
            self.matrice[jeton.ligne][jeton.colonne] = Jeton()
                
    def nombreJetons(self):
        return 42-len(self.historique)
    
    def state(self, jeton: Jeton):
        
        if len(self.historique)==42:
            return 2 #plateau plein
        else:
            if isinstance(jeton, Jeton):
                ligne = self.matrice[jeton.ligne]
                colonne = self.matrice[:, jeton.colonne]
                diagonale1 = np.diagonal(self.matrice, offset=jeton.colonne - jeton.ligne)
                diagonale2 = np.diagonal(np.fliplr(self.matrice), offset=(self.matrice.shape[1]-jeton.colonne-1)-jeton.ligne)

                for i in range(len(ligne)):
                    if ligne[i].couleur != "blanc":
                        try:
                            if ligne[i].couleur == ligne[i+1].couleur == ligne[i+2].couleur == ligne[i+3].couleur:
                                return 1 #gagné
                        except IndexError:
                            pass
                                
                for i in range(len(colonne)):
                    if colonne[i].couleur != "blanc":
                        try:
                            if colonne[i].couleur == colonne[i+1].couleur == colonne[i+2].couleur == colonne[i+3].couleur:
                                return 1 #gagné
                        except IndexError:
                            pass
    
                for i in range(len(diagonale1)):
                    if diagonale1[i].couleur != "blanc":
                        try:
                            if diagonale1[i].couleur == diagonale1[i+1].couleur == diagonale1[i+2].couleur == diagonale1[i+3].couleur:
                                return 1 #gagné
                        except IndexError:
                            pass

                for i in range(len(diagonale2)):
                    if diagonale2[i].couleur != "blanc":
                        try:
                            if diagonale2[i].couleur == diagonale2[i+1].couleur == diagonale2[i+2].couleur == diagonale2[i+3].couleur:
                                return 1 #gagné
                        except IndexError:
                            pass
                                
                return 0 #partie en cours
            else:
                return -1 #erreur
            
 