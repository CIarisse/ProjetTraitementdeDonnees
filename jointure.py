# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import table

from table import Table
from transformations.transformation import Transformation

class Jointure(Transformation) :
    """Classe permettant de joindre 2 tables de jeux de données avec une variable commune
        
    Attributes
    ---------
    table : Table
        liste de listes contenant les données
    variables : list
        liste avec la variable commune
    table2 : Table
        liste de listes contenant les données à joindre à la première table
    
    Example
    -------
    >>> t =  Table([["var1","var2","var3","var4"],
    ...    [5,"oui","NA","NA"],
    ...    [8,"non",87,"NA"],
    ...   [4,"oui",2.9,97]])
    >>> t2 = Table([["var3","var5","var6","var4"],
    ...    ["NA","oui","NA","NA"],
    ...   [87,"oui",87,35],
    ...   [2.9,"non",65,97]])
    >>> d = Jointure(t, ['var3','var4'], t2)
    >>> print(d.transforme().donnees)
    [['var1', 'var2', 'var3', 'var4', 'var3', 'var5', 'var6', 'var4'], [5, 'oui', 'NA', 'NA', 'NA', 'oui', 'NA', 'NA'], [4, 'oui', 2.9, 97, 2.9, 'non', 65, 97]]
    """
    def __init__(self, table, variables, table2):
        """Constructeur"""
        Transformation.__init__(self, table, variables)
        self.table2 = table2

    def transforme(self):
        """Permet de joindre deux tables données en attributs avec une variable commune si celle ci 
        a bien des colonnes identiques dans les 2 tables

        
        Returns
        ------
        nouvelle_table : Table
            table résultat de la jointure sur la variable commune
        """
        #si pas de variable commune clef : erreur
        if len(self.variables) == 0:
            print("Erreur : il faut au moins 1 variable clef")
            return None     

        colonnes1 = []
        colonnes2 = []
        var1 = []
        var2 = []
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes1.append(self.table.donnees[0].index(self.variables[i]))
            colonnes2.append(self.table2.donnees[0].index(self.variables[i]))
            # colonnes1 et colonnes2 récupèrent les indices des colonnes des variables que l'on veut traiter
                #si variable commune clef pas dans 2 tables : erreur

        if len(colonnes1) != len(self.variables) or len(colonnes2) != len(self.variables):
            print("Erreur : Les variables clefs ne sont pas toutes présentes dans la première table")
            return None

        for i in range(len(self.table.donnees)):
            var1.append([])
            for c1 in colonnes1:
                var1[i].append(self.table.donnees[i][c1])

        for j in range(len(self.table2.donnees)):
            var2.append([])
            for c2 in colonnes2:
                var2[j].append(self.table2.donnees[j][c2])

        nouvelle_table=[]

        for i in range(len(var1)):
            for j in range(len(var2)):
                if var1[i] == var2[j] :
                    nouvelle_table.append(self.table.donnees[i] + self.table2.donnees[j])

        return Table(nouvelle_table)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

