from table import Table
from transformation import Transformation
from datetime import datetime


class Temporel(Transformation) :
    """Classe qui permettra de sélectionner des données comprises entre deux dates
    
    Attributes
    ----------
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à considérer
    date_debut : date
        borne inférieure des dates à conserver
    date_fin : date
        borne supérieure des dates à conserver
    """
    
    def __init__(self, table, variables, date_debut, date_fin):
        """Constructeur"""
        Transformation.__init__(self, table, variables)
        self.date_debut = date_debut
        self.date_fin = date_fin

    def transforme(self):
        #si plus de 1 variable ou pas variable : erreur
        if len(self.variables) > 1 or len(self.variables) == 0:
            print("Erreur : il faut 1 variable à filtrer")
            return None

        nouvelle_table = Table([])
        for i in range(len(self.table.donnees[0])): #on parcourt le nom des variables de Table
            if self.variables[0] == self.table.donnees[0][i]: #si on retrouve le nom de la variable dans Table
                nouvelle_table.donnees.append(self.table.donnees[0])
                for j in range(1,len(self.table.donnees)): #on parcourt les lignes
                    var_date = self.table.donnees[j][i]
                    var_formate = datetime(int(var_date[0:4]), int(var_date[4:6]), int(var_date[6:8]),int(var_date[8:10], int(var_date[10:12])), int(var_date[12:14]))
                    if var_formate < self.date_fin and var_formate > self.date_debut: #si valeur dans notre colonne est bien dans dates demandees
                        nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur
        return nouvelle_table

 


#convertisse en date
#var tester et valeurs soient même type 

test = Table([["var1","var2","var3","var4"],
              ["20220526150000","oui","NA","NA"],
              ["20220529180000","non","87","NA"],
              ["20220613140000","oui","2.9","97"]])

print(datetime(2022,5,27))
print(datetime(2022,6,10))


temp = Temporel(test, ["var1"], datetime(2022,5,27), datetime(2022,6,10))
print(temp.table.donnees)
res = temp.transforme()
print(res.donnees)
