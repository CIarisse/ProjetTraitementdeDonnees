import statistics

from table import Table
from transformation import Transformation


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
    >>> t = Table([["var1","var2","var3","var4"],
              ["5","oui","NA","NA"],
              ["8","non","87","NA"],
              ["4","oui","2.9","97"]])
    >>> s = Spatial(t)
    >>> print(s.transforme().donnees)
    [['var1', 'var2', 'var3', 'var4'], 
     [5.67, 'NA', 44.95, 97.0]]
    
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
        nouvelle_table = Table([[0]*len(self.table.donnees[0])]*2) #creer une nouvelle table de 2 lignes et d'autant de colonnes que de variables
        nouvelle_table.donnees[0] = self.table.donnees[0] #ajout 1er ligne avec nom variables
        temp = []

        for i in range(len(self.table.donnees[0])): #on parcourt les colonnes
            for j in range(len(self.table.donnees)): #on parcourt les lignes
                try:
                    float(self.table.donnees[j][i])
                    temp.append(float(self.table.donnees[j][i]))
                except ValueError:
                    continue     
            if len(temp) != 0 :
                nouvelle_table.donnees[1][i] = round(statistics.mean(temp),2)
            else :
                nouvelle_table.donnees[1][i] = 'NA'
            temp = []
        return nouvelle_table

