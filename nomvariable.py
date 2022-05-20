class NomVariable(Transformation) :
    def __init__(self, nouveau_nom):
        self.nouveau_nom = nouveau_nom
        Transformation.__init__()

    def transforme(self):
        nouvelle_table = self.table #on copie la table
        for i in range(len(self.variables)): #on parcourt le nom des variables à modifier
            for j in range(len(nouvelle_table.donnees[0])): #on parcourt les noms des variables de la Table
                if self.variables[i] == nouvelle_table.donnees[0][j]: #si le nom est retrouve dans la table
                    nouvelle_table.donnees[0][j] = self.nouveau_nom[i] #on modifie le nom
        return nouvelle_table



#revoir bien avec attributs de Table


