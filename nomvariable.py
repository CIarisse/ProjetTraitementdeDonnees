from table import Table
from transformation import Transformation

class NomVariable(Transformation) :
    def __init__(self, table, variables, nouveau_nom):
        Transformation.__init__(self, table, variables)
        self.nouveau_nom = nouveau_nom

    def transforme(self):
        nouvelle_table = self.table #on copie la table
        for i in range(len(self.variables)): #on parcourt le nom des variables à modifier
            for j in range(len(nouvelle_table.donnees[0])): #on parcourt les noms des variables de la Table
                if self.variables[i] == nouvelle_table.donnees[0][j]: #si le nom est retrouve dans la table
                    nouvelle_table.donnees[0][j] = self.nouveau_nom[i] #on modifie le nom
        return nouvelle_table


test = Table([["var1","var2","var3","var4"],
              ["5","oui","NA","NA"],
              ["8","non","87","NA"],
              ["4","oui","2.9","97"]])
transf = Transformation(test,["var2"])
print(transf.table.donnees)
nomvar = NomVariable(test, ["var4","var2"], ["nveau","essai"])
print(nomvar.table.donnees)
res = nomvar.transforme()
print(res.donnees)


