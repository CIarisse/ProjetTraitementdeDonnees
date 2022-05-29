from transformation import Transformation
from table import Table

class DonneesQuali(Transformation) :
    """Classe permettant de filtrer les données qualitatives selon les valeurs prises par les variables qualitatives considérées
    
    Attributes
    ---------
    table : Table
        liste de listes contenant les données
    variables : list
        liste avec la variable à filtrer
    valeurs : list
        liste des modalités à conserver de la variable qualitative
    
    Example
    -------
    >>> t = Table([["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])
    >>> d = DonneesQuali(t, ['var2'], "oui")
    >>> print(d.transforme().donnees)
    [["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [4,"oui",2.9,56],
              [9,"oui",25,"NA"]]
    
    
    """
    def __init__(self, table, variables, valeurs):
        """Constructeur"""
        Transformation.__init__(self, table, variables)
        self.valeurs = valeurs

    def transforme(self):
        """Permet de filtrer une variable qualitatitive, seules les lignes ayant comme valeur à cette variable une 
        des valeurs que l'on souhaite garder (valeurs : list) sont présentes en sortie

        
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
                    for k in range(len(self.valeurs)): #on parcourt les valeurs qui nous interessent
                        if self.table.donnees[j][i] == self.valeurs[k]: #si valeur dans notre colonne a bien valeur demande 
                            nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur
        return nouvelle_table

