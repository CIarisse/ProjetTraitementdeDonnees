from estimation import Estimation
import statistics

class ValeursExtremes(Estimation):
    """Calsse permettant de gérer les valeurs extrêmes.
    
    Les données seront soit supprimées, soit remplacées par la VAI ou VAS"""

    def __init__(self, table, variables):
        """Constructeur"""
        super().__init__(table, variables)

    
    def estime(self, methode, a, manquante):
        """Remplace les valeurs extrêmes
        
        Remplace les valeurs supérieures à Q3+1.5(Q3-Q1) par cette valeur,
        et les valeurs inférieures à Q1-1.5(Q3-Q1) par cette valeur (methode = 'extremes'),
        ou supprime les lignes contenenant ces valeurs extremes (methode = 'suppression')

        Attributes
        ----------
        methode : str
            méthode à utiliser pour gérer les valeurs extrêmes

        a : int
            précision de la valeur de remplacement

        manquante : str
            format des données manquantes (ex : 'mq', 'NA')

        Returns
        -------
        sortie : Table
            table dont les valeurs extrêmes ont été traitées pour les variables considérées
        """

        sortie = self.table.donnees # copie de la table : c'est cette copie qui sera modifiée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter
        for c in colonnes: # pour tous les indices des colonnes à traiter
            valeurs = []

            if methode == 'extremes':
                for k in range(1,n):
                    if self.table.donnees[k][c] != manquante :
                        valeurs.append(float(self.table.donnees[k][c]))
                q1 = round(statistics.quantiles(valeurs)[0],a) # valeur du premier quartile
                q3 = round(statistics.quantiles(valeurs)[2],a) # valeurs du troisième quartile
                inf = q1-1.5*(q3-q1)
                sup = q3+1.5*(q3-q1)
                for l in range(1,n) : # retour aux données de la table 'sortie' en parcourant ses lignes
                    if sortie[l][c] != manquante :
                        if float(sortie[l][c]) < inf :
                            sortie[l][c] = inf
                        elif float(sortie[l][c]) > sup :
                            sortie[l][c] = sup

            if methode == 'suppression':
                for k in range(1,n):
                    if self.table.donnees[k][c] != manquante :
                        valeurs.append(float(self.table.donnees[k][c]))
                q1 = round(statistics.quantiles(valeurs)[0],a) # valeur du premier quartile
                q3 = round(statistics.quantiles(valeurs)[2],a) # valeurs du troisième quartile
                inf = q1-1.5*(q3-q1)
                sup = q3+1.5*(q3-q1)
                i = 1
                while i < len(sortie) and sortie[i][c] != manquante :
                    if float(sortie[i][c]) < 10 or float(sortie[i][c]) > 100 :
                        del sortie[i]
                    else :
                        i += 1
        return sortie
