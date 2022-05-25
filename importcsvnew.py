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
    def __init__(self, donnees = []):
        ''' Création d'une table grâce aux données
        Parameters
        ----------
        donnees : list, default []
            L'ensemble des données sous forme de liste de listes

        '''
        self.donnees = donnees

    def importcsv(chemin):
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
        with open(chemin, encoding='ISO-8859-1') as csvfile :
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)
        self.donnees = data


    def import_json(chemin,nom):
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
        >>>test2.import_json("P:\Projet_info",r"\test2.json.gz")
        >>>print(test2.donnees)
    
        """
        # Dossier où se trouve le fichier :
        folder = chemin
        filename = nom
        with gzip.open(folder + filename, mode='rt') as gzfile :
            data = json.load(gzfile)

        #ici data est une liste de dictionnaires

        #on cherche les variables
        var=[]
        nb_var=0
        list_doubledict=[]
        for i in range(len(data)):
            nom_col=list(data[i].keys())
            nom_colonnes=list(data[i].keys())
            k=0
            for j in nom_col:
                if isinstance(data[i][j],dict):
                    nom_colonnes+=list(data[i][j].keys())
                    del(nom_colonnes[k])
                    list_doubledict.append([j,len(list(data[i][j].keys()))])
                k+=1
            var.append([nom_colonnes,len(nom_colonnes)])
            nb_var=max(nb_var,var[i][1])
        for i in range(len(data)):
            if nb_var==var[i][1]:
                noms_var=var[i][0]
        lignes=[]
        for i in range(len(data)):
            var_par_obs=var[i][0]
            nb_var_par_obs=var[i][1]
            l=[]
            compte_col=0 #car j est un str
            for j in noms_var:
                if j not in var_par_obs:
                    l.append("mq")
                elif compte_col<nb_var_par_obs-list_doubledict[i][1]:
                    l.append(data[i][j])
                else:
                    l.append(data[i][list_doubledict[i][0]][j])
                compte_col+=1
            lignes.append(l)
        self.donnees = list_doubledict


        
        
        
#Tableau1=importcsv("P:\Projet_info\postesSynop.csv")
#print(Tableau1)
#a = Table("2013-02.json.gz","P:\Projet_info\donnees_elec\2013-02.json.gz")
#Tableau2=Table.import_json(a)
#print(Tableau2)
tab2 = Table()
tab2.import_json("P:\Projet_info",r"\test2.json.gz")
print(tab2.donnees)
#tab2.import_json()




