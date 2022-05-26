from table import Table
from transformation import Transformation

class DonneesQuanti(Transformation) :
    def __init__(self, table, variables, borne_inf, borne_sup):
        Transformation.__init__(self, table, variables)
        self.borne_inf = borne_inf
        self.borne_sup = borne_sup

    def transforme(self):
        #si plus de 1 variable ou pas variable : erreur
        if len(self.variables) > 1 or len(self.variables) == 0:
            print("Erreur : il faut 1 variable à filtrer")
            return None

        nouvelle_table = Table([])
        nouvelle_table.donnees.append(self.table.donnees[0])
        for i in range(len(self.table.donnees[0])): #on parcourt le nom des variables de Table
            if self.variables[0] == self.table.donnees[0][i]: #si on retrouve le nom de la variable dans Table
                for j in range(1,len(self.table.donnees)): #on parcourt les lignes
                    try:
                        if float(self.table.donnees[j][i]) < self.borne_sup and float(self.table.donnees[j][i]) > self.borne_inf: #si valeur dans notre colonne est bien dans bornes demandees
                            nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur
                    except ValueError:
                        continue     
        return nouvelle_table


test = Table([["var1","var2","var3","var4"],
              ["5","oui","NA","NA"],
              ["8","non","87","NA"],
              ["4","oui","2.9","97"]])
transf = Transformation(test,["var2"])
print(transf.table.donnees)
doquanti = DonneesQuanti(test, ["var4"], 75, 100)
print(doquanti.table.donnees)
res = doquanti.transforme()
print(res.donnees)
