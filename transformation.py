class Transformation() :
    """Permet d'instancier un type de transfomation. Classe abstraite, dont héritent :
    
    Jointure : joindre des jeux de données de type Table
    NomVariable : modifier le nom des variables
    SelectionVa : sélectionner variable
    DonneesQuanti : sélectionner des observations selon valeurs de données quantitatives
    DonneesQuali : sélectionner des observations selon valeurs de données qualitatives
    Spatial : passage d'un niveau régional à un niveau national
    
    Attributs
    ---------
        table : Table
            table que l'on souhaite estimer/modifier
        variables : list
            liste des variables sur lesquelles ont souhaite appliquer les méthodes
    """
    
    
    def __init__(self, table, variables):
        self.table = table
        self.variables = variables

    def transforme(self):
        pass

