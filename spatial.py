from curses.ascii import isdigit
from unicodedata import numeric
from donneesquali import DonneesQuali
import statistics


class Spatial(Transformation) :
    def __init__(self,):
        Transformation.__init__()

    def transforme(self):
         #agrégation spatiale : passage régional au national
        #fonction statistics.mean(liste) pour moyenne

        nouvelle_table = Table([[0]*len(self.table.donnees[0])]*2) #creer une nouvelle table de 2 lignes et d'autant de colonnes que de variables
        nouvelle_table.donnees[0] = self.table.donnees[0] #ajout 1er ligne avec nom variables
        temp = []

        for i in range(len(self.table.donnees[0])): #on parcourt les colonnes
            for j in range(len(self.table.donnees)): #on parcourt les lignes
                try:
                    float(self.table.donnees[j][i])
                    temp.append(self.table.donnees[j][i])
                except ValueError:
                    continue     
            if len(temp) != 0 :
                nouvelle_table.donnees[1][i] = statistics.mean(temp)
            else :
                nouvelle_table.donnees[1][i] = 'NA'
            temp = []
        return nouvelle_table