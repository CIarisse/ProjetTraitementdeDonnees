from estimation import Estimation
from table import Table
import statistics

class DonneesManquantes(Estimation):
    """Classe permettant de gérer les données manquantes
    Les données seront soit supprimées, soit remplacées par la moyenne de la variable
    
    table : Table
        ensemble des données en liste de listes
    variables : list
        liste des noms des variales à considérer
    arrondi : int = 2
        nombre de décimales pour le calcul des statistiques
        
    Example
    ------
    >>> t = Table([["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])
    >>> d = DonneesManquante(t,['var3'])
    >>> print(d.estime('suppression')
    [["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [8,"non",7.9,13.6]]
    
    """

    def __init__(self, table, variables, arrondi = 2):
        """Constructeur"""
        Estimation.__init__(self,table, variables, arrondi)


    def estime(self, methode):
        """ Remplace les valeurs manquantes des variables considérées.
        Plusieurs possibilités : suppression entière de la ligne, (methode = 'suppression')
        remplacement de la valeur manquante par la moyenne de la variable (methode = 'moyenne'),
        ou remplacement de la valeur manquante par la médiane de la variable (methode = 'mediane')
        
        Parameters
        ----------
        methode : str
            méthode à utiliser pour gérer les données manquantes



        Returns
        -------
        sortie : Table
            table dont les données manquantes ont été traitées pour les variables considérées
        """

        if len(self.variables) == 0 or methode not in ('moyenne','mediane','suppression'):
            print("Erreur : il faut au moins 1 variable pour traiter avec 1 méthode donnée ('moyenne','mediane','suppression')")
            return None            

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
                    if self.table.donnees[k][c] != 'NA':
                        valeurs.append(self.table.donnees[k][c])
                moy = round(statistics.mean(valeurs),self.arrondi)
                
            # puis retour aux données de la table 'sortie'
                for l in range(len(sortie)) :  # parcours des lignes
                    if sortie[l][c] == 'NA' :
                        sortie[l][c] = moy # remplacement de la données manquante par la moyenne de la variable

            if methode == 'mediane':
                for k in range(1,n):
                    if self.table.donnees[k][c] != 'NA' :
                        valeurs.append(self.table.donnees[k][c])
                med = round(statistics.median(valeurs),self.arrondi)
                
                
                for l in range(len(sortie)) : # retour aux données de la table 'sortie' en parcourant ses lignes
                    if sortie[l][c] == 'NA':
                        sortie[l][c] = med

            if methode == 'suppression':
                i = 1
                while i < len(sortie):
                    if sortie[i][c] == 'NA' :
                        del sortie[i]
                    else :
                        i += 1

        return Table(sortie)



test = Table([["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])

test2 = Table([["var5","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])

est2 = DonneesManquantes(test,["var4"])
essai = est2.estime('moyenne')

print(est2.table.donnees)
print(est2.variables)
print(test.donnees)
print(essai.donnees)

est1 = DonneesManquantes(test2,["var3"])
est1.estime('moyenlne')


print(est1.table.donnees)
print(est1.variables)
