from table import Table
from transformation import Transformation

class DonneesQuanti(Transformation) :
    """Classe permettant de filtrer les données quantitatives selon un intervalle de valeurs
    
    Attributes
    ---------
    table : Table
        liste de listes contenant les données
    variables : list
        liste avec la variable à filtrer
    borne_inf : float
        borne inférieure des valeurs à conserver
    borne_sup : float
        borne supérieure des valeurs à conserver
    
    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
    ...          [5,"oui","NA",76],
    ...          [8,"non",87,67.9],
    ...          [4,"oui",2.9,56],
    ...          [3,"non",66,78.9],
    ...          [9,"oui",25,"NA"],
    ...          [8,"non",7.9,13.6]])
    >>> d = DonneesQuanti(t, ['var1'], 3, 6)
    >>> print(d.transforme().donnees)
    [['var1', 'var2', 'var3', 'var4'], [5, 'oui', 'NA', 76], [4, 'oui', 2.9, 56]]
    """
    
    def __init__(self, table, variables, borne_inf, borne_sup):
        """Constructeur"""
        Transformation.__init__(self, table, variables)
        self.borne_inf = borne_inf
        self.borne_sup = borne_sup

    def transforme(self):
        """Permet de filtrer une variable quantitative, seules les lignes ayant comme valeur à cette variable une 
        valeur étant entre les deux bornes exclus (borne_inf : int et borne_sup :int) sont présentes en sortie

        
        Returns
        ------
        nouvelle_table : Table
            table modifiée dont les valeurs de la variable considérée ont été filtrées
        """
        #si plus de 1 variable ou pas variable : erreur
        if len(self.variables) > 1 or len(self.variables) == 0:
            print("Erreur : il faut 1 variable à filtrer")
            return None

        nouvelle_table = Table([])
        nouvelle_table.donnees.append(self.table.donnees[0])
        for i in range(len(self.table.donnees[0])): #on parcourt le nom des variables de Table
            if self.variables[0] == self.table.donnees[0][i]: #si on retrouve le nom de la variable dans Table
                for j in range(1,len(self.table.donnees)): #on parcourt les lignes
                    if self.table.donnees[j][i] != 'NA' : 
                        if self.table.donnees[j][i] < self.borne_sup and self.table.donnees[j][i] > self.borne_inf: #si valeur dans notre colonne est bien dans bornes demandees
                            nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur            
        return nouvelle_table

if __name__ == "__main__":
    import doctest
    doctest.testmod()