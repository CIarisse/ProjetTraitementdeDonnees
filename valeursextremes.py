from estimation import Estimation
from table import Table
import statistics

class ValeursExtremes(Estimation):
    """Classe permettant de gérer les valeurs extrêmes.
    
    Les données seront soit supprimées, soit remplacées par la Q3+1.5(Q3-Q1) ou Q1-1.5(Q3-Q1)
    
    Attributes
    ----------
    table : Table
        table que l'on souhaite estimer/modifier
    variables : list
        liste des variables sur lesquelles ont souhaite appliquer les méthodes

    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",100000, 67.9],
    ...          [4,"oui",2.9, 56],
    ...          [3,"non",6.36, 78.9],
    ...          [9,"oui",2.5, "NA"],
    ...          [8,"non",7.9, 13.6],
    ...          [4,"oui",2.9, 56],
    ...          [3,"non",6.36, 78.9],
    ...          [9,"oui",2.5, "NA"],
    ...          [8,"non",7.9, 13.6],
    ...          [4,"oui",2.9, 56]])
    >>> d = ValeursExtremes(t, ['var3'])
    >>> print(d.estime('suppression').donnees)
    [['var1', 'var2', 'var3', 'var4'], [5, 'oui', 'NA', 76], [4, 'oui', 2.9, 56], [3, 'non', 6.36, 78.9], [9, 'oui', 2.5, 'NA'], [8, 'non', 7.9, 13.6], [4, 'oui', 2.9, 56], [3, 'non', 6.36, 78.9], [9, 'oui', 2.5, 'NA'], [8, 'non', 7.9, 13.6], [4, 'oui', 2.9, 56]]
    """

    def __init__(self, table, variables, arrondi = 2):
        """Constructeur"""
        Estimation.__init__(self,table, variables, arrondi)

    
    def estime(self, methode):
        """Remplace les valeurs extrêmes
        
        Remplace les valeurs supérieures à Q3+1.5(Q3-Q1) par cette valeur,
        et les valeurs inférieures à Q1-1.5(Q3-Q1) par cette valeur (methode = 'extremes'),
        ou supprime les lignes contenenant ces valeurs extremes (methode = 'suppression')

        Attributes
        ----------
        methode : str
            méthode à utiliser pour gérer les valeurs extrêmes

        Returns
        -------
        sortie : Table
            table dont les valeurs extrêmes ont été traitées pour les variables considérées
        """
        if len(self.variables) == 0 or methode not in ('extremes','suppression'):
            print("Erreur : il faut au moins 1 variable pour traiter avec 1 méthode donnée ('extremes','suppression')")
            return None 


        sortie = self.table.donnees # copie de la table : c'est cette copie qui sera modifiée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter
        for c in colonnes: # pour tous les indices des colonnes à traiter
            valeurs = []

            if methode == 'extremes':
                for k in range(1,n):
                    if self.table.donnees[k][c] != 'NA' :
                        valeurs.append(self.table.donnees[k][c])
                q1 = round(statistics.quantiles(valeurs)[0],self.arrondi) # valeur du premier quartile
                q3 = round(statistics.quantiles(valeurs)[2],self.arrondi) # valeurs du troisième quartile
                inf = round(q1-1.5*(q3-q1),self.arrondi)
                sup = round(q3+1.5*(q3-q1),self.arrondi)
                for l in range(1,n) : # retour aux données de la table 'sortie' en parcourant ses lignes
                    if sortie[l][c] != 'NA' :
                        if sortie[l][c] < inf :
                            sortie[l][c] = inf
                        elif sortie[l][c] > sup :
                            sortie[l][c] = sup

            if methode == 'suppression':
                for k in range(1,n):
                    if self.table.donnees[k][c] != 'NA' :
                        valeurs.append(self.table.donnees[k][c])
                q1 = round(statistics.quantiles(valeurs)[0],self.arrondi) # valeur du premier quartile
                q3 = round(statistics.quantiles(valeurs)[2],self.arrondi) # valeurs du troisième quartile
                inf = round(q1-1.5*(q3-q1),self.arrondi)
                sup = round(q3+1.5*(q3-q1),self.arrondi)


                i = 1
                while i < len(sortie):
                    if sortie[i][c] != 'NA' :
                        if sortie[i][c] < inf or sortie[i][c] > sup :
                            del sortie[i]
                        else:
                            i += 1
                    else :
                        i += 1
                    
        return Table(sortie)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
