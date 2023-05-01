class Jeton:

    def __init__(self, ligne: int= None, colonne: int= None, couleur: str= "blanc"):
        self.ligne = ligne
        self.colonne = colonne
        self.couleur = couleur

    def __str__(self):
        return f"Jeton de couleur {self.couleur} en colonne ({self.colonne} et ligne {self.ligne})"
    
    
    