class Temporel(Transformation) :
    def __init__(self, date_debut, date_fin):
        self.date_debut = date_debut
        self.date_fin = date_fin
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
                    if self.table.donnees[j][i] < self.date_fin and self.table.donnees[j][i] > self.date_debut: #si valeur dans notre colonne est bien dans dates demandees
                        nouvelle_table.donnees.append(self.table.donnees[j]) #ajout de la ligne avec la bonne valeur
        return nouvelle_table
