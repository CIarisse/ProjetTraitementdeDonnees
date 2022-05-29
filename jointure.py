# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

from table import Table
from transformation import Transformation

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
    ...        [5,"oui","NA","NA"],
    ...        [8,"non",87,"NA"],
    ...        [4,"oui",2.9,97]])
    >>> t2 = Table([["var3","var5","var6","var7"],
    ...        ["NA","oui","NA",87],
    ...        [87,"oui",87,35],
    ...        [2.9,"non",65,93]])
    >>> d = Jointure(t, ['var3'], t2)
    >>> print(d.transforme().donnees)
    [['var1', 'var2', 'var3', 'var4', 'var5', 'var6', 'var7'], [5, 'oui', 'NA', 'NA', 'oui', 'NA', 87], [8, 'non', 87, 'NA', 'oui', 87, 35], [4, 'oui', 2.9, 97, 'non', 65, 93]]
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
        #si plus de 1 variable ou pas variable ou nb lignes des tables different : erreur
        if len(self.variables) > 1 or len(self.variables) == 0 or (len(self.table.donnees) != len(self.table2.donnees)):
            print("Erreur : il faut 1 variable à filtrer et le même nombre de lignes pour les 2 tables")
            return None     

        nouvelle_table=Table()


        #on recopie le premier tableau
        comp = 0
        var = []
        for k in range(len(self.table.donnees)): #parcourt lignes
            nouvelle_table.donnees.append([])
            for i in range(len(self.table.donnees[0])): #parcourt colonnes
                if self.variables[0] != self.table.donnees[0][i]:
                    comp += 1
                else :
                    var.append(self.table.donnees[k][i])
                nouvelle_table.donnees[k].append(self.table.donnees[k][i]) 
        if comp == len(self.table.donnees[0]):
            print("Erreur : La variable clef n'est pas présente dans la première table")
            return None  
  
        #on recopie le deuxieme tableau sans la colonne commune
        comp = 0
        var2 = []
        for l in range(len(self.table2.donnees)): #parcourt lignes
            for j in range(len(self.table2.donnees[0])): #parcourt colonnes
                if self.table2.donnees[0][j] != self.variables[0]:
                    nouvelle_table.donnees[l].append(self.table2.donnees[l][j]) 
                    comp += 1
                else :
                    var2.append(self.table2.donnees[l][j])

        if comp == len(self.table2.donnees[0]):
            print("Erreur : La variable clef n'est pas présente dans la deuxième table")
            return None  

        if var != var2:
            print("Erreur : Les 2 colonnes de la variable clef ne sont pas les mêmes")
            return None

        return nouvelle_table

if __name__ == "__main__":
    import doctest
    doctest.testmod()