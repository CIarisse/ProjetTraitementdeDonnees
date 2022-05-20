class Jointure(Transformation) :
    def __init__(self, table2):
        self.table2 = table2
        Transformation.__init__()

    def transforme(self):
        #si plus de 1 variable : erreur
        if len(self.variables):
            print("Erreur : plus de 1 variable comme clef")
            return None        

        #erreur si pas variable clef
    
        nouvelle_table = Table([[0]*(len(self.table.donnees[0])+len(self.table2.donnees[0]))]*len(self.table.donnees)))
        for i in range(len(self.table.donnees[0])):
            for k in range(len(self.table.donnees)):
                nouvelle_table.donnees[k][i] = [self.table.donnees[k][i]]
        for j in range(len(self.table.donnees[0]),len(self.table2.donnees[0])):
            for l in range(len(self.table.donnees)):
                nouvelle_table.donnees[l][j] = [self.table2.donnees[l][j-len(self.table.donnees[0])]]
        return nouvelle_table

