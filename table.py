import csv
import json
import gzip


class Table():
    '''Classe qui gère les tables et les imports/exports suivant les formats

    Attributes
    ----------
    donnees : list, default []
        les donnees sous format de liste de listes


    Examples
    --------
    >>>postes = Table()
    >>>postes.importcsv("P:\Projet_info\postesSynop.csv")
    >>>print(postes.donnees)
    
    '''
    def __init__(self, nom_colonnes = [], donnees = []):
        ''' Création d'une table grâce aux données
        Parameters
        ----------
        donnees : list, default []
            L'ensemble des données sous forme de liste de listes

        '''
        self.nom_colonnes = nom_colonnes
        self.donnees = donnees
        

    def importcsv(self,chemin, manquante):
        '''Importation d'une table au format csv
        Parameters
        ----------
        chemin : str 
            Le chemin où se trouve le fichier csv

        Examples
        --------
        >>>postes = Table()
        >>>postes.importcsv("P:\Projet_info\postesSynop.csv")
        >>>print(postes.donnees)
            
        '''
        data = []
        with open(chemin, mode='rt', encoding='utf-8') as csvfile :
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)

        
        res = []
        for i in range(1,len(data)):
            res.append([])
            for j in range(len(data[0])):
                valeur = data[i][j]
                try:
                    valeur = int(valeur)
                except ValueError:
                    try:
                        valeur = float(valeur)
                    except ValueError:
                        pass
                if valeur == manquante:
                        valeur = 'NA'
                res[i-1].append(valeur)

        self.nom_colonnes = data[0]
        self.donnees = res




    def import_json(self,chemin):
        """'''Importation d'une table au format json
        Parameters
        ----------
        chemin : str 
            Le chemin où se trouve le fichier json
        nom : str 
            Le nom du fichier qui contient les donnees 

        Examples
        --------
        >>>test2 = Table()
        >>>test2.import_json("P:\Projet_info\test2.json.gz")
        >>>print(test2.donnees)
    
        """
        # Dossier où se trouve le fichier :
        with gzip.open(chemin, mode = "rt", encoding = "utf-8") as gzfile:
            data = json.load(gzfile)
        data = [obs["fields"] for obs in data]


        #On importe les noms de nos variables
        dictionnaire = {}
        
        for ligne in data:
                for nom_variable in ligne:
                    if not nom_variable in dictionnaire:
                        dictionnaire[nom_variable]=[]
        variables = list(dictionnaire.keys())

        #importation de nos données
        for ligne in data:
            for variable in dictionnaire:
                if variable in ligne:
                    dictionnaire[variable].append(ligne[variable])
                else:
                    dictionnaire[variable].append('NA')

        #Finalement on a la table suivante
        donnees = []
        for variable in dictionnaire:
            for j in range(len(dictionnaire[variable])):
                if variable == variables[0]:
                    donnees.append([])
                valeur = dictionnaire[variable][j]
                try:
                    valeur = int(valeur)
                except ValueError:
                    try:
                        valeur = float(valeur)
                    except ValueError:
                        pass
                donnees[j].append(valeur)


        self.donnees = donnees
        self.nom_colonnes = variables
        
        

        
        
#Tableau1=importcsv("P:\Projet_info\postesSynop.csv")
#print(Tableau1)
#a = Table("2013-02.json.gz","P:\Projet_info\donnees_elec\2013-02.json.gz")
#Tableau2=Table.import_json(a)
#print(Tableau2)


tab = Table()
tab.importcsv("D:\Documents\Ecole\ENSAI 1A\projet_info\codes_transformation\donnees\synop.201301.csv",'mq')
print(tab.nom_colonnes)
print(tab.donnees[0:6])

tab2 = Table()
tab2.import_json("D:/Documents/Ecole/ENSAI 1A/projet_info/codes_transformation/donnees/2013-01.json.gz")
print(tab2.donnees[0:6])
print(tab2.nom_colonnes)

