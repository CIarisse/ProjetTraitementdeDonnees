class selectionVa(Transformation) :
    def __init__(self):
        Transformation.__init__()

    def transforme(self):
        nouvelle_table = Table([[0]*len(self.variables)]*len(self.table.donnees)) #on cree une table avec nb colonnes = nb variables à selectionner et nb lignes = nb lignes de Table
        for i in range(len(self.variables)): #on parcourt le nom des variables à sélectionner
            for j in range(len(self.table.donnees[0])): #on parcourt le nom des variables de la Table
                if self.variables[i] == self.table.donnees[0][j]: #si le nom est retrouve dans la Table
                    for k in range(len(self.table.donnees)): #on parcourt les lignes de la Table
                        nouvelle_table.donnees[k][i] = [self.table.donnees[k][j]] #on copie la colonne
        return nouvelle_table

#revoir bien avec attributs de Table
           