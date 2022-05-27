from estimation import Estimation
import statistics

class Normalisation(Estimation):
    """Classe permettant de gérer le centrage et la normalisation des variables"""

    def __init__(self, table, variable):
        """Constructeur"""
        super().__init__(table, variable)

    
    def estime(self, methode, a, manquante) :
        """Permet de centrer ou normaliser les variables considérées

        Parameters
        ---------
        methode : str
            methode à appliquer : 'centrage' ou 'normalisation'
        a : int
            arrondi des valeurs calculées
        manquante : str
            format des données manquantes (ex : "NA", "mq")

        
        Returns
        ------
        sortie : Table
            table modifiée dont les variables considérées ont été soit centrées, soit normées
        """

        sortie = self.table.donnees # copie de la table : c'est cette copie qui sera modifiée puis retournée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter
        for c in colonnes :
            valeurs = []
            # récupération de l'ensemble des valeurs pour la variable en indice c
            # (y compris valeurs manquantes)
            for k in range(1,n):
                if self.table.donnees[k][c] != manquante :
                    valeurs.append(float(self.table.donnees[k][c])) # ensemble des valeurs non manquantes de la valeur considérée
            moy = statistics.mean(valeurs)
            sd = statistics.stdev(valeurs)
            for i in range(1,n) :
                if methode == 'centrage' and sortie[i][c] != manquante : 
                    sortie[i][c] = round(float(sortie[i][c])-moy,a)
                elif methode == 'normalisation' and sortie[i][c] != manquante :
                    sortie[i][c] = round(float((sortie[i][c]))-moy/sd,a)

        return sortie
