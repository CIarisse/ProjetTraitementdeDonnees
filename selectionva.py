from table import Table
from transformation import Transformation

class SelectionVa(Transformation) :
    def __init__(self, table, variables):
        Transformation.__init__(self, table, variables)

    def transforme(self):
        nouvelle_table=Table()

        for i in range(len(self.variables)): #on parcourt le nom des variables à sélectionner
            for j in range(len(self.table.donnees[0])): #on parcourt le nom des variables de la Table

                if self.variables[i] == self.table.donnees[0][j]: #si le nom est retrouve dans la Table
                    
                    for k in range(len(self.table.donnees)):
                        if i == 0:
                            nouvelle_table.donnees.append([])
                        nouvelle_table.donnees[k].append(self.table.donnees[k][j]) 
                
        return nouvelle_table

        

test = Table([["var1","var2","var3","var4"],
              ["5","oui","NA","NA"],
              ["8","non","87","NA"],
              ["4","oui","2.9","97"]])
transf = Transformation(test,["var2"])
print(transf.table.donnees)
selvar = SelectionVa(test, ["var4","var2"])
print(selvar.table.donnees)
res = selvar.transforme()
print(res.donnees)
           