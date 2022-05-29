from estimation import Estimation
from table import Table
import statistics

class Centrage(Estimation):
    """Classe permettant de gérer le centrage et la normalisation des variables
    
    Attributes
    ---------
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à considérer
    arrondi : int = 2
        nombre de décimales pour le calcul des statistiques
        
    Example
    ------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",87,67.9],
    ...          [4,"oui",2.9,56],
    ...          [3,"non",66,78.9],
    ...          [9,"oui",25,"NA"],
    ...          [8,"non",7.9,13.6]])
    >>> c = Centrage(t, ["var4"])
    >>> print(c.estime('centrer').donnees)
    [['var1', 'var2', 'var3', 'var4'], [5, 'oui', 'NA', 17.52], [8, 'non', 87, 9.42], [4, 'oui', 2.9, -2.48], [3, 'non', 66, 20.42], [9, 'oui', 25, 'NA'], [8, 'non', 7.9, -44.88]]
    """

    def __init__(self, table, variables, arrondi = 2):
        """Constructeur"""
        Estimation.__init__(self, table, variables, arrondi)

    
    def estime(self, methode) :
        """Permet de centrer ou normaliser les variables considérées

        Parameters
        ---------
        methode : str
            methode à appliquer : 'centrer' ou 'normer'
        
        Returns
        ------
        sortie : Table
            table modifiée dont les variables considérées ont été soit centrées, soit normées
        """
        if len(self.variables) == 0 or methode not in ('centrer','normer'):
            print("Erreur : il faut au moins 1 variable pour calculer 1 méthode donnée ('centrer','normer')")
            return None        

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
                if self.table.donnees[k][c] != 'NA' :
                    valeurs.append(self.table.donnees[k][c]) # ensemble des valeurs non manquantes de la valeur considérée
            moy = statistics.mean(valeurs)
            sd = statistics.stdev(valeurs)
            for i in range(1,n) :
                if methode == 'centrer' and sortie[i][c] != 'NA': 
                    sortie[i][c] = round(sortie[i][c]-moy,self.arrondi)
                elif methode == 'normer' and sortie[i][c] != 'NA' :
                    sortie[i][c] = round((sortie[i][c]-moy)/sd,self.arrondi)

        return Table(sortie)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
