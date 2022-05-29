# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent

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
from table import Table

class Pipeline():
    def __init__(self, operations=[]):
        """ constructeur 
        
        Parameters
        ----------
        
        """
        self.operations = operations


    def ajoute(self,operation):
        self.operations.append(operation)


    def execute(self, table):
        for operation in self.operations:

            '''
            if ('Centrage' or 'MoyenneGlissante' or 'DonneesManquantes' or 'Statistique' or 'ValeursExtremes') in operation:
                estimation = operation[0:operation.find('(')]
                print(estimation)
                var = operation[operation.find('['):operation.find(']')+1]
                methode = operation[operation.find(',')+1:operation.find(')')]
                inst = estimation(table, var)
                res = inst.estime(methode)
                table = res

            if ('DonneesQuanti' or 'DonneesQuali' or 'Jointure' or 'NomVariable' or 'SelectionVa' or 'Spatial' or 'Temporel') in operation:
                transformation = operation[0:operation.find('(')]
                var = operation[operation.find('['):operation.find(']')+1]
                res = transformation(self.table,var).transforme()
                table = res
            '''

test = Table([["var1","var2","var3","var4"],
              [5,"oui","NA",76],
              [8,"non",87,67.9],
              [4,"oui",2.9,56],
              [3,"non",66,78.9],
              [9,"oui",25,"NA"],
              [8,"non",7.9,13.6]])

essai = Pipeline()
essai.ajoute('Centrage(["var4"])')
print(essai.operations)
essai.execute(test)