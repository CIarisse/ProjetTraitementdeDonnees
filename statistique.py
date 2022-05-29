# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

from estimation import Estimation
from table import Table
import statistics

class Statistique(Estimation):
    """Correspond à une statistique d'une ou plusieurs variables d'une table
    (moyenne, médiane, variance, ecart_type)
    
    Attributes
    ----------
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à considérer
    arrondi : int = 2
        nombre de décimale pour le résultat
        
    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",87,67.9],
    ...          [4,"oui",2.9,56],
    ...          [3,"non",66,78.9],
    ...          [9,"oui",25,"NA"],
    ...          [8,"non",7.9,13.6]])
    >>> s = Statistique(t,['var1','var3'])
    >>> print(s.estime('moyenne'))
    [6.17, 37.76]
    """

    def __init__(self, table, variables, arrondi=2):
        """ Constructeur """
        Estimation.__init__(self, table, variables, arrondi)


    def estime(self, stat):
        """ Calcule la statistique de(s) la (les) variables considérées 
        stat peut prendre les valeurs suivantes : 'moyenne', 'mediane', 'variance'
        
        Parameters
        ----------
        stat : str
            nom de la statistique à appliquer

        Returns
        -------
        res : list[float]
            resultats de la statistique calculee
        """

        if len(self.variables) == 0 or stat not in ('moyenne','mediane','variance'):
            print("Erreur : il faut au moins 1 variable pour calculer 1 statistique donnée ('moyenne','mediane','variance')")
            return None  

        colonnes = []
        res = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut étudier
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut étudier
        for c in colonnes : # pour tous les indices des colonnes que l'on doit étudier
            valeurs = []
            if stat == 'moyenne' :
                sum = 0
                t = 0
                for k in range(1,n):
                    if self.table.donnees[k][c] != 'NA' :
                        sum += self.table.donnees[k][c]
                        t += 1 # nombre de valeurs non manquantes
                res.append(round(sum/t,self.arrondi))

            elif stat == 'mediane' :
                for k in range(1,n) : # pour toutes les données (pour chaque ligne)
                    if self.table.donnees[k][c] != 'NA' : # on ne prend pas les valeurs manquantes
                        valeurs.append(self.table.donnees[k][c])
                valeurs.sort() # liste de toutes les valeurs de la variable de la colonne j
                if len(valeurs)%2 != 0 : # nombre impair de valeurs
                    mediane = valeurs[int((len(valeurs)-1)/2)]
                else : # nombre pair de valeurs
                    mediane = (valeurs[int((len(valeurs)/2)-1)] + valeurs[int(len(valeurs)/2)])/ 2
                res.append(round(mediane,self.arrondi))

            elif stat == 'variance' :
                for k in range(1,n) : # pour toutes les lignes de cette variable
                    if self.table.donnees[k][c] != 'NA' : # on ne prend pas les valeurs manquantes
                        valeurs.append(self.table.donnees[k][c])
                res.append(round(statistics.pvariance(valeurs),self.arrondi))
        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
