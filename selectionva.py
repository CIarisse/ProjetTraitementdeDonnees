# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import table

from table import Table
from transformations.transformation import Transformation

class SelectionVa(Transformation) :
    """Classe permettant de ne sélectionner que les variables qui nous intéressent
    
    Attributes
    ----------
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à considérer
        
    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",87,67.9],
    ...          [4,"oui",2.9,56],
    ...          [3,"non",66,78.9]])
    >>> s = SelectionVa(t,['var1','var4'])
    >>> print(s.transforme().donnees)
    [['var1', 'var4'], [5, 76], [8, 67.9], [4, 56], [3, 78.9]]
    
    """
    
    
    def __init__(self, table, variables):
        """Constructeur"""
        Transformation.__init__(self, table, variables)

    def transforme(self):
        """Permet de sélectionner certaines colonnes par leur nom de variable

        Returns
        ------
        nouvelle_table : Table
            table modifiée avec uniquement les colonnes de variables attendues
        """
        nouvelle_table=[]

        for i in range(len(self.variables)): #on parcourt le nom des variables à sélectionner
            for j in range(len(self.table.donnees[0])): #on parcourt le nom des variables de la Table

                if self.variables[i] == self.table.donnees[0][j]: #si le nom est retrouve dans la Table
                    
                    for k in range(len(self.table.donnees)):
                        if i == 0:
                            nouvelle_table.append([])   
                        nouvelle_table[k].append(self.table.donnees[k][j]) 
                
        return Table(nouvelle_table)


if __name__ == "__main__":
    import doctest
    doctest.testmod()