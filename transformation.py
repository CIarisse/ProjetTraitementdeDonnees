from abc import ABC, abstractmethod

class Transformation(ABC) :
    """Permet d'instancier un type de transfomation. Classe abstraite, dont héritent :
    
    Jointure : joindre des jeux de données de type Table
    NomVariable : modifier le nom des variables
    SelectionVa : sélectionner variable
    DonneesQuanti : sélectionner des observations selon valeurs de données quantitatives (dont la classe Temporel découle)
    DonneesQuali : sélectionner des observations selon valeurs de données qualitatives
    Spatial : passage d'un niveau régional à un niveau national
    
    Attributs
    ---------
        table : Table
            table que l'on souhaite estimer/modifier
        variables : list
            liste des variables sur lesquelles on souhaite appliquer les méthodes
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
    def transforme(self):
        pass
