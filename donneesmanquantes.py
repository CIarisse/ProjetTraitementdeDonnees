from estimation import Estimation
import statistics

class DonneesManquantes(Estimation):
    """Classe permettant de gérer les données manquantes
    Les données seront soit supprimées, soit remplacées par la moyenne de la variable
    """

    def __init__(self, table, variable):
        """Constructeur"""
        super().__init__(table, variable)


    def estime(self,methode, a, manquante):
        """ Remplace les valeurs manquantes des variables considérées.
        Plusieurs possibilités : suppression entière de la ligne, (methode = 'suppression')
        remplacement de la valeur manquante par la moyenne de la variable (methode = 'moyenne'),
        ou remplacement de la valeur manquante par la médiane de la variable (methode = 'mediane')
        
        Attributes
        ----------
        methode : str
            méthode à utiliser pour gérer les données manquantes

        a : int
            précision de la valeur de remplacement

        manquante : str
            format des données manquantes (ex : 'mq', 'NA')

        Returns
        -------
        sortie : Table
            table dont les données manquantes ont été traitées pour la variable considérées
        """

        sortie = self.table # copie de la table : c'est cette copie qui sera modifiée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter
        for c in colonnes: # pour tous les indices des colonnes à traiter

            if methode == 'moyenne':
                moy = []
                valeurs = []
                for k in range(1,n): # pour toutes les lignes de cette variable
                    valeurs.append(self.table.donnees[k][j])
                moy.append(round(statistics.mean(valeurs),a))
                # res est un vecteur de la longueur du nombre de variables à traiter, contant les moyennes de ces variables
            # puis retour aux données de la table 'sortie'
                for l in range(len(self.table.donnees)) :  # parcours des lignes
                    if sortie[l][c] == manquante :
                        sortie[l][c] = moy[c] # remplacement de la données manquante par la moyenne de la variable

            if methode == 'mediane':
                med = []
                valeurs = []
                for k in range(1,n):
                    valeurs.append(self.table.donnees[k][j])
                med.append(round(statistics.median(valeurs),a))
                for l in range(len(self.table.donnees)) : # retour aux données de la table 'sortie'
                    if sortie[l][c] == manquante :
                        sortie[l][c] = med[c]

            if methode == 'suppression':
                for l in range(len(self.table.donnees)):
                    if self.table.donnees == manquante :
                        del sortie[l] # supprimer toute la ligne contenant la données manquante
            
            return sortie

