from estimation import Estimation
import statistics

class Statistique(Estimation):
    """Correspond à une statistique d'une ou plusieurs variables d'une table
    (moyenne, médiane, variance, ecart_tyoe)"""

    def __init__(self, table, variables):
        """ Constructeur """
        super().__init__(table, variables)


    def estime(self, stat, a, manquante):
        """ Calcule la statistique de(s) la (les) variables considérées 
        stat peut prendre les valeurs suivantes : 'moyenne', 'mediane', 'variance'
        
        Attributes
        ----------
        stat : str
            nom de la statistique à appliquer
        a : int
            précision de la statistique retournée
        manquante : str
            format des données manquantes (ex : 'NA', 'mq')

        Returns
        -------
        res : [float]
            resultat de la statistique calculee
            """
        colonnes = []
        res = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut étudier
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut étudier
        for c in colonnes : # pour tous les indices des colonnes que l'on doit étudier

            if stat == 'moyenne' :
                sum = 0
                t = 0
                for j in colonnes : # pour tous les indices des colonnes à traiter
                    for k in range(1,n):
                        if self.table.donnees[k][j] != manquante :
                            sum += float(self.table.donnees[k][j])
                            t += 1 # nombre de valeurs non manquantes
                    res.append(round(sum/t,a))

            elif stat == 'mediane' :
                valeurs = [] # sera la liste de toutes les données de la variable d'indice j
                for j in colonnes : # pour tous les indices des colonnes à traiter
                    for k in range(1,n) : # pour toutes les données (pour chaque ligne)
                        if self.table.donnees[k][j] != manquante : # on ne prend pas les valeurs manquantes
                            valeurs.append(float(self.table.donnees[k][j]))
                    valeurs.sort() # liste de toutes les valeurs de la variable de la colonne j
                    if len(valeurs)%2 != 0 : # nombre impair de valeurs
                        mediane = valeurs[(len(valeurs)-1)/2]
                    else : # nombre pair de valeurs
                        mediane = (valeurs[(len(valeurs)-1)/2] + valeurs[len(valeurs)+1/2])/ 2
                    res.append(round(mediane,a))

            elif stat == 'variance' :
                valeurs = [] # sera la liste de toutes les données de la variable d'indice j
                for j in colonnes : # pour tous les indices des colonnes à traiter
                    for k in range(1,n) : # pour toutes les lignes de cette variable
                        valeurs.append(float(self.table.donnees[k][j]))
                    res.append(round(statistics.pvariance(valeurs),a))

            return res





