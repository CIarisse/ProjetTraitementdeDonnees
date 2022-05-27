from estimation import Estimation
import statistics

class DonneesManquantes(Estimation):
    """Classe permettant de gérer les données manquantes
    Les données seront soit supprimées, soit remplacées par la moyenne de la variable
    """

    def __init__(self, table, variable):
        """Constructeur"""
        super().__init__(table, variable)


    def estime(self, methode, a, manquante):
        """ Remplace les valeurs manquantes des variables considérées.
        Plusieurs possibilités : suppression entière de la ligne, (methode = 'suppression')
        remplacement de la valeur manquante par la moyenne de la variable (methode = 'moyenne'),
        ou remplacement de la valeur manquante par la médiane de la variable (methode = 'mediane')
        
        Parameters
        ----------
        methode : str
            méthode à utiliser pour gérer les données manquantes

        a : int
            précision de la valeur de remplacement (utile seulement pour 'moyenne' et 'mediane')

        manquante : str
            format des données manquantes (ex : 'mq', 'NA')

        Returns
        -------
        sortie : Table
            table dont les données manquantes ont été traitées pour les variables considérées
        """

        sortie = self.table.donnees # copie de la table : c'est cette copie qui sera modifiée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter

        for c in colonnes: # pour tous les indices des colonnes à traiter
            valeurs = []
            
            if methode == 'moyenne':
                for k in range(1,n): # pour toutes les lignes de cette variable
                    if self.table.donnees[k][c] != manquante :
                        valeurs.append(float(self.table.donnees[k][c]))
                moy = round(statistics.mean(valeurs),a)
                # res est un vecteur de la longueur du nombre de variables à traiter, contant les moyennes de ces variables
            # puis retour aux données de la table 'sortie'
                for l in range(len(self.table.donnees)) :  # parcours des lignes
                    if sortie[l][c] == manquante :
                        sortie[l][c] = moy # remplacement de la données manquante par la moyenne de la variable

            if methode == 'mediane':
                for k in range(1,n):
                    if self.table.donnees[k][c] != manquante :
                        valeurs.append(float(self.table.donnees[k][c]))
                med = round(statistics.median(valeurs),a)
                for l in range(len(self.table.donnees)) : # retour aux données de la table 'sortie' en parcourant ses lignes
                    if sortie[l][c] == manquante :
                        sortie[l][c] = med

            if methode == 'suppression':
                i = 1
                while i < len(sortie):
                    if sortie[i][c] == manquante :
                        del sortie[i]
                    else :
                        i += 1

        return sortie
