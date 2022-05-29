# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

from abc import ABC, abstractmethod

class Estimation(ABC):
    """Permet d'instancier un type d'estimation. Classe abstraite
    
    Estimation retournant une statistique de variable : Statistique
    Gestion des données manquantes (retourne une table) : DonneeesManquantes
    Gestion des valeurs extrêmes (retourne une table) : ValeursExtremes
    Calcul d'une moyenne glissante (retourne une table avec une colonne supplémentaire) : MoyenneGlissante
    Centrer des variables (retourne une table) : Centrage

    Attributs
    ---------
        table : Table
            table que l'on souhaite estimer/modifier
        variables : list
            liste des variables sur lesquelles on souhaite appliquer les méthodes
        arrondi : int
            précision de l'arrondi pour nos estimations

    """

    def __init__(self, table, variables, arrondi):
        """ constructeur 
        
        Parameters
        ----------
        table : Table
            table sur laquelle on travaille
        variables : list
            liste de variables sur lesquelles on travaille
        arrondi : int
            précision de l'arrondi pour nos estimations
        """
        self.table = table
        self.variables = variables
        self.arrondi = arrondi

    @abstractmethod
    def estime():
        pass