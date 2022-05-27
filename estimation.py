from abc import ABC, abstractmethod

class Estimation(ABC):
    """Permet d'instancier un type d'estimation. Classe abstraite
    
    Estimation retournant une statistique de variable : Statistique
    Gestion des données manquantes (retourne une table) : DonneeesManquantes
    Gestion des valeurs extrêmes (retourne une table) : ValeursExtremes
    Calcul d'une moyenne glissante : retourne une table à une dimension
    Centrer des variables : Centrage

    Attributs
    ---------
        table : Table
            table que l'on souhaite estimer/modifier
        varialbe : list
            liste des variables sur lesquelles ont souhaite appliquer les méthodes

    Examples
    --------
    """

    def __init__(self, table, variables):
        """ constructeur 
        
        Parameters
        ----------
        table : Table
            table sur laquelle on travaille
        variables : list
            liste de variables sur lesquelles on travaille
        """
        self.table = table
        self.variables = variables

    @abstractmethod
    def estime():
        pass
