# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent


import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import table

import statistics
from table import Table
from transformations.transformation import Transformation


class Spatial(Transformation) :
    """Classe qui permet, via la méthode transforme, de passer de données régionales à des données nationales
    
    Attributes
    ----------
    table : Table
        ensemble des données en liste de listes
    variables : list=[]
        liste des noms des variales à considérer

    Example
    -------
    >>> t = Table([['var1', 'var2', 'var3', 'var4'], 
    ...                [5, 'oui', 'NA', 76], 
    ...                [8, 'non', 87, 67.9], 
    ...                [4, 'oui', 2.9, 56], 
    ...                [3, 'non', 66, 78.9], 
    ...                [9, 'oui', 25, 'NA'], 
    ...                [8, 'non', 7.9, 13.6]])
    >>> s = Spatial(t)
    >>> print(s.transforme().donnees)
    [['var1', 'var2', 'var3', 'var4'], [6.17, 'NA', 37.76, 58.48]]
    
    """
    
    def __init__(self,table,variables=[]):
        """Constructeur"""
        Transformation.__init__(self, table, variables)

    def transforme(self):
        """Permet d'effectuer une aggrégation spatiale en passant de données régionales (avec plusieurs lignes) à des 
        données nationales (une seule ligne étant la moyenne des données régionales)

        Returns
        ------
        nouvelle_table : Table
            table modifiée avec une seule ligne correspondante à l'aggrégation nationale
        """
        nouvelle_table = [[0]*len(self.table.donnees[0])]*2 #creer une nouvelle table de 2 lignes et d'autant de colonnes que de variables
        nouvelle_table[0] = self.table.donnees[0] #ajout 1er ligne avec nom variables
        temp = []

        for i in range(len(self.table.donnees[0])): #on parcourt les colonnes
            for j in range(len(self.table.donnees)): #on parcourt les lignes
                if isinstance(self.table.donnees[j][i], int) or isinstance(self.table.donnees[j][i], float):
                    temp.append(self.table.donnees[j][i])
            if len(temp) != 0 :
                nouvelle_table[1][i] = round(statistics.mean(temp),2)
            else :
                nouvelle_table[1][i] = 'NA'
            temp = []
        return Table(nouvelle_table)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
