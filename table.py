# Projet Info 1A 2022
# Clarisse Dubois, Eva Puchalski et Eva Vincent


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
    >>> test = Table([["var1","var2","var3","var4"],
    ...                    [5,"oui","NA",76],
    ...                    [8,"non",87,67.9],
    ...                    [4,"oui",2.9,56],
    ...                    [3,"non",66,78.9],
    ...                    [9,"oui",25,"NA"],
    ...                    [8,"non",7.9,13.6]])
    >>> test.export("D:/Documents/Ecole/ENSAI 1A/projet_info/codes/donnees","test_export")
    >>> nveau = Table()
    >>> nveau.importcsv("D:/Documents/Ecole/ENSAI 1A/projet_info/codes/donnees/test_export.csv",'NA')
    >>> print(nveau.donnees)
    [['var1', 'var2', 'var3', 'var4'], [5, 'oui', 'NA', 76], [8, 'non', 87, 67.9], [4, 'oui', 2.9, 56], [3, 'non', 66, 78.9], [9, 'oui', 25, 'NA'], [8, 'non', 7.9, 13.6]]
    '''
    def __init__(self, donnees = []):
        ''' Création d'une table grâce aux données
        Parameters
        ----------
        donnees : list, default []
            L'ensemble des données sous forme de liste de listes

        '''
        self.donnees = donnees
        

    def importcsv(self,chemin, manquante):
        '''Importation d'une table au format csv
        Parameters
        ----------
        chemin : str 
            Le chemin où se trouve le fichier csv

        manquante : str
            format des données manquantes dans la table

        Examples
        --------
        >>> nveau = Table()
        >>> nveau.importcsv("D:/Documents/Ecole/ENSAI 1A/projet_info/codes/donnees/test_export.csv",'NA')
        >>> print(nveau.donnees)
        [['var1', 'var2', 'var3', 'var4'], [5, 'oui', 'NA', 76], [8, 'non', 87, 67.9], [4, 'oui', 2.9, 56], [3, 'non', 66, 78.9], [9, 'oui', 25, 'NA'], [8, 'non', 7.9, 13.6]]
        '''
        data = []
        with open(chemin, mode='rt', encoding='utf-8') as csvfile :
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)

        
        res = []
        for i in range(len(data)):
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
                res[i].append(valeur)

        self.donnees = res




    def importjson(self,chemin):
        """Importation d'une table au format json
        Parameters
        ----------
        chemin : str 
            Le chemin où se trouve le fichier json

        Examples
        --------
        >>> tab2 = Table()
        >>> tab2.importjson("D:/Documents/Ecole/ENSAI 1A/projet_info/codes/donnees/2013-01.json.gz")
        >>> print(tab2.donnees[0:6])
        [['code_insee_region', 'date', 'region', 'date_heure', 'heure', 'consommation_brute_gaz_terega', 'statut_terega', 'consommation_brute_electricite_rte', 'statut_rte', 'consommation_brute_gaz_grtgaz', 'consommation_brute_totale', 'consommation_brute_gaz_totale', 'statut_grtgaz'], [24, '2013-01-01', 'Centre-Val de Loire', '2013-01-01T00:00:00+01:00', '00:00', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'], [75, '2013-01-01', 'Nouvelle-Aquitaine', '2013-01-01T00:00:00+01:00', '00:00', 1775, 'Définitif', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'], [11, '2013-01-01', 'Île-de-France', '2013-01-01T00:30:00+01:00', '00:30', 'NA', 'NA', 9134, 'Définitif', 'NA', 'NA', 'NA', 'NA'], [24, '2013-01-01', 'Centre-Val de Loire', '2013-01-01T00:30:00+01:00', '00:30', 'NA', 'NA', 2476, 'Définitif', 'NA', 'NA', 'NA', 'NA'], [76, '2013-01-01', 'Occitanie', '2013-01-01T00:30:00+01:00', '00:30', 'NA', 'NA', 5228, 'Définitif', 'NA', 'NA', 'NA', 'NA']]
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

        #Table finale avec les conversions
        donnees = [variables]
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
                donnees[j+1].append(valeur)


        self.donnees = donnees
        

    def export(self,chemin, nom_fichier):
        """Exportation d'une table vers un fichier csv
        Parameters
        ----------
        chemin : str 
            Le chemin où on veut placer le fichier
        nom_fichier : str
            Le nom qu'on le veut donner au fichier

        Examples
        --------
        >>> test = Table([["var1","var2","var3","var4"],
        ...                    [5,"oui","NA",76],
        ...                    [8,"non",87,67.9],
        ...                    [4,"oui",2.9,56],
        ...                    [3,"non",66,78.9],
        ...                    [9,"oui",25,"NA"],
        ...                    [8,"non",7.9,13.6]])
        >>> test.export("D:/Documents/Ecole/ENSAI 1A/projet_info/codes/donnees","test_export")
        """
        resultat=[]
        for i in range(len(self.donnees)):
            resultat.append(self.donnees[i])
        with open('{}/{}.csv'.format(chemin,nom_fichier), 'w', newline='',encoding='UTF8') as csvfile:
            sortie = csv.writer(csvfile,delimiter=';')
            sortie.writerows(resultat)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
