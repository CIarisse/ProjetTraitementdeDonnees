from estimation import Estimation
from table import Table
import statistics


def extrait(liste, milieu, taille):
    """Retourne une liste de longueur taille, dont l'élément milieu est au milieu (si taille impaire);
    et une place avant le milieu (si taille paire)
    
    Parameters
    ---------
    liste : list
        liste dont on veut extraire les éléments
    milieu : int
        indice de l'élément du milieu de la liste 
    taille : 
        longueur de la liste extraite
    
    Return
    ------
    sortie : list
        liste extraite
    
    Example
    ------
    >>> l = [1,2,1,3,4,5,6,7]
    >>> print(extrait(l, 2, 3)
    [2,1,3] 
    """
    if taille % 2 != 0 : # si taille impaire
        sortie = liste[int(max(0,milieu-((taille-1)/2))) : int(min(milieu+((taille-1)/2),len(liste))+1)]
    else : # si taille paire
        sortie = liste[int(max(0,milieu-((taille/2)-1))) : int(min(milieu+(taille/2),len(liste))+1)]
    return sortie


class MoyenneGlissante(Estimation):
    '''Classe permettant de gérer la moyenne glissante

    La moyenne glissante modifie une table (liste de listes), et
    renvoie une table contenant dans chaque case la moyenne des n valeurs 
    alentours (n doit être impair)
    '''

    def __init__(self, table, variables, arrondi = 2):
        """Constructeur"""
        Estimation.__init__(self, table, variables, arrondi)

    
    def estime(self, pas):
        '''Renvoie la moyenne glissante des variables considérées
        
        Parameters
        ----------
        pas : int
            taille du fenêtrage pour le calcul de la moyenne glissante

        Returns
        -------
        sortie : Table
            table dont les moyennes glissantes ont été traitées pour les variables considérées
        '''

        if len(self.variables) == 0 or pas < 2:
            print("Erreur : il faut au moins 1 variable et un pas d'au moins 2 pour effectuer le calcul")
            return None 

        sortie = self.table.donnees # copie de la table : c'est cette copie qui sera modifiée puis retournée
        colonnes = []
        n = len(self.table.donnees) # nombre de lignes de la table
        for i in range(len(self.variables)) : # pour toutes les variables qu'on veut traiter
            colonnes.append(self.table.donnees[0].index(self.variables[i]))
            # colonnes récupère les indices des colonnes des variables que l'on veut traiter
        
        for c in colonnes :
            valeurs = []
            # récupération de l'ensemble des valeurs pour la variable en indice c
            # (y compris valeurs manquantes)
            for k in range(1,n):
                if self.table.donnees[k][c] != 'NA' :
                    valeurs.append(self.table.donnees[k][c]) # les valeurs non manquantes sont mises en float
                else : 
                    valeurs.append(self.table.donnees[k][c]) # on remet aussi les valeurs manquantes
            # valeurs contient l'ensemble des valeurs de la variable considérée (colonne c)
            moygliss = [None]*len(valeurs)
            for i in range(len(valeurs)): # parcourt tous les éléments de la liste valeurs
                temp = []
                temp_na = extrait(valeurs,i,pas)
                for elt in temp_na :
                    if elt != 'NA':
                        temp.append(elt) # temp correspond aux valeurs du fenêtrage qui ne sont pas des données manquantes
                if len(temp) == 0 : # seulement des données manquantes dans la fenêtre considérées
                    moygliss[i] = 'NA' # donnée manquante dans la moyenne glissante
                else :
                    moygliss[i] = round(statistics.mean(temp),self.arrondi)
            # ajouter une colonne à sortie qui va contenir nos moyennes glissantes
            sortie[0].append('moygliss{}'.format(c)) # nom de la colonne
            for p in range(1,n):
                sortie[p].append(moygliss[p-1])
        return Table(sortie)



test = Table([["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])

est2 = MoyenneGlissante(test,["var4"])
essai = est2.estime(1)

print(est2.table.donnees)