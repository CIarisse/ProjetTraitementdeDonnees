# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

from table import Table
from estimation import Estimation
from transformation import Transformation
from centrage import Centrage
from donneesmanquantes import DonneesManquantes
from donneesquali import DonneesQuali
from donneesquanti import DonneesQuanti
from jointure import Jointure
from moyenneglissante import MoyenneGlissante
from nomvariable import NomVariable
from selectionva import SelectionVa
from spatial import Spatial
from statistique import Statistique
from temporel import Temporel
from valeursextremes import ValeursExtremes



class Pipeline():
    def __init__(self, operations=[]):
        """ constructeur 
        
        Parameters
        ----------
        operations : list = []
            liste des opérations à effectuer sur une table
        
        Example
        -------
        >>> test = Table([["var1","var2","var3","var4"],
        ...          [5,"oui","NA",76],
        ...          [8,"non",87,67.9],
        ...          [4,"oui",2.9,56],
        ...          [3,"non",66,78.9],
        ...          [9,"oui",25,"NA"],
        ...          [8,"non",7.9,13.6]])
        >>> essai = Pipeline()
        >>> essai.ajoute(NomVariable(test,["var3"], ['Score']))
        >>> essai.ajoute(SelectionVa(test,['Score',"var4"]))
        >>> essai.ajoute([Centrage(test,["var4"]),'centrer'])
        >>> essai.ajoute(NomVariable(test,["var4"], ['Releve']))
        >>> essai.ajoute([DonneesManquantes(test,["Releve"]), 'moyenne'])
        >>> print(essai.execute(test).donnees)
        [['Score', 'Releve'], ['NA', 17.52], [87, 9.42], [2.9, -2.48], [66, 20.42], [25, -0.0], [7.9, -44.88]]

        """
        self.operations = operations


    def ajoute(self,operation):
        """Permet d'ajouter une opération à la liste des opérations d'une Pipeline

        Parameters
        ----------
        operation : Transformation ou list[Estimation, str]
            transformation ou estimation à ajouter à notre Pipeline

        """
        self.operations.append(operation)


    def execute(self,table):
        """Permet d'éxécuter la liste des opérations contenues dans la Pipeline sur la table

        Parameters
        ----------
        table : Table
            table sur laquelle éxécuter les transformations / estimations

        """
        for operation in self.operations:
            if isinstance(operation,Transformation):
                    operation.table = table
                    table = operation.transforme()

            elif isinstance(operation[0],Estimation) :
                operation[0].table = table
                table = operation[0].estime(operation[1])
        return table

if __name__ == "__main__":
    import doctest
    doctest.testmod()

