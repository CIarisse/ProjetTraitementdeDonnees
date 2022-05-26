from table import Table
from transformation import Transformation

class Jointure(Transformation) :
    def __init__(self, table, variables, table2):
        Transformation.__init__(self, table, variables)
        self.table2 = table2

    def transforme(self):
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



test = Table([["var1","var2","var3","var4"],
              ["5","oui","NA","NA"],
              ["8","non","87","NA"],
              ["4","oui","2.9","97"]])
join = Table([["var3","var5","var6","var7"],
              ["NA","oui","NA","87"],
              ["87","oui","87","35"],
              ["2.9","non","65","93"]])
#nouvelle_table = Table([[0]*(len(test.donnees[0])+len(self.table2.donnees[0]))]*len(self.table.donnees))
#print(len(test.donnees))
transf = Transformation(test,["var3"])
#print(transf.table.donnees)
#print(join.donnees)
joindre = Jointure(test, ["var3"], join)
print(joindre.table.donnees)
print(joindre.table2.donnees)
res = joindre.transforme()
print(res.donnees)
