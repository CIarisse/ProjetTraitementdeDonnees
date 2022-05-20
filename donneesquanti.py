#from table import Table

class DonneesQuanti(Transformation) :
    def __init__(self, borne_inf, borne_sup):
        self.borne_inf = borne_inf
        self.borne_sup = borne_sup
        Transformation.__init__()

    def transforme(self):
        #si plus de 1 variable : erreur
        if len(self.variables):
            print("Erreur : plus de 1 variable à filtrer")
            return None

        nouvelle_table = Table([])
        for i in range(len(self.table.donnees[0])): #on parcourt le nom des variables de Table
            if self.variables[0] == self.table.donnees[0][i]: #si on retrouve le nom de la variable dans Table
                for j in range(1,len(self.table.donnees)): #on parcourt les lignes
                    if self.table.donnees[j][i] < self.borne_sup and self.table.donnees[j][i] > self.borne_inf: #si valeur dans notre colonne est bien dans bornes demandees
                        nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur
        return nouvelle_table
