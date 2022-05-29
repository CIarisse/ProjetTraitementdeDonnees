# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

from table import Table
from transformation import Transformation

class NomVariable(Transformation) :
    """ Classe permettant de modifier les noms des variables
    
    Attributes
    ----------
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à modifier
    nouveau_nom : list
        liste des nouveaux noms à donner aux variables considérées
    
    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",87,67.9]])
    >>> n = NomVariable(t,['var1','var3'],['A','C'])
    >>> print(n.transforme().donnees)
    [['A', 'var2', 'C', 'var4'], [5, 'oui', 'NA', 76], [8, 'non', 87, 67.9]]
    
    
    """
    def __init__(self, table, variables, nouveau_nom):
        """Constructeur"""
        Transformation.__init__(self, table, variables)
        self.nouveau_nom = nouveau_nom

    def transforme(self):
        """Permet de modifie le nom des variables données en leur donnant un nouveau nom souhaité

        Returns
        ------
        nouvelle_table : Table
            table modifiée dont les noms des variables ont été changés
        """
        nouvelle_table = self.table #on copie la table
        for i in range(len(self.variables)): #on parcourt le nom des variables à modifier
            for j in range(len(nouvelle_table.donnees[0])): #on parcourt les noms des variables de la Table
                if self.variables[i] == nouvelle_table.donnees[0][j]: #si le nom est retrouve dans la table
                    nouvelle_table.donnees[0][j] = self.nouveau_nom[i] #on modifie le nom
        return nouvelle_table

if __name__ == "__main__":
    import doctest
    doctest.testmod()