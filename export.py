class Export():
    def __init__(self,chemin,nom_fichier):
        self.chemin=chemin
        self.nom_fichier=nom_fichier

    def export(self,table):
        resultat=[table.nom_variables]
        for i in range(len(table.donnees)):
            resultat.append(table.selection_ligne(i))
        with open('{}/{}.csv'.format(self.chemin,self.nom_fichier), 'w', newline='',encoding='UTF8') as csvfile:
            sortie = csv.writer(csvfile,delimiter=',')
            sortie.writerows(resultat)
