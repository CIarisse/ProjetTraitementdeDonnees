from datetime import datetime
from pipeline import Pipeline
from table import Table
from estimations.estimation import Estimation
from transformations.transformation import Transformation
from estimations.centrage import Centrage
from estimations.donneesmanquantes import DonneesManquantes
from transformations.donneesquali import DonneesQuali
from transformations.donneesquanti import DonneesQuanti
from transformations.jointure import Jointure
from estimations.moyenneglissante import MoyenneGlissante
from transformations.nomvariable import NomVariable
from transformations.selectionva import SelectionVa
from transformations.spatial import Spatial
from estimations.statistique import Statistique
from transformations.temporel import Temporel
from estimations.valeursextremes import ValeursExtremes

# import table meteo
meteo = Table()
meteo.importcsv("D:/Documents/Ecole/ENSAI_1A/projet_info/rendu_codes/donnees/synop.201301.csv","mq")
#print(meteo.donnees[0:10])

# import table conso
conso = Table()
conso.importjson("D:/Documents/Ecole/ENSAI_1A/projet_info/rendu_codes/donnees/2013-01.json.gz")
#print(conso.donnees[0:10])

# import table des postes meteo avec regions
region = Table()
region.importcsv("D:/Documents/Ecole/ENSAI_1A/projet_info/rendu_codes/donnees/postesSynopAvecRegions.csv","")
#print(region.donnees[0:10])

# renommage pour la jointure
nom_sta = NomVariable(region,['ID'],['numer_sta'])
region = nom_sta.transforme()

# jointure avec region, selection variables et renommage pour future jointure
res = Pipeline()
res.ajoute(Jointure(meteo,['numer_sta'], region))
res.ajoute(SelectionVa(meteo,['date','t','tn12','tn24','tx12','tx24','tminsol','numer_sta','Region']))
res.ajoute(NomVariable(meteo,['date','Region'],['date_heure','region']))
meteo_rg = res.execute(meteo)
#print(meteo_rg.donnees[0:10])
#print(len(meteo_rg.donnees))

# conversion en format date des dates de meteo et conso pour la jointure
for i in range(1,len(meteo_rg.donnees)):
    meteo_rg.donnees[i][0] = datetime.strptime(str(meteo_rg.donnees[i][0]),'%Y%m%d%H%M%S')

for j in range(1,len(conso.donnees)):
    conso.donnees[j][3] = str(conso.donnees[j][3])[0:19]
    conso.donnees[j][3] = datetime.strptime(conso.donnees[j][3],'%Y-%m-%dT%H:%M:%S')

# on vide Pipeline, on effectue jointure avec conso, traitement des données manquantes et normalisation de variables
res.operations = []
res.ajoute(Jointure(meteo_rg,['date_heure','region'],conso))
res.ajoute([DonneesManquantes(meteo_rg,['consommation_brute_totale']),"moyenne"])
res.ajoute([Centrage(meteo_rg,['t','consommation_brute_gaz_terega','consommation_brute_electricite_rte','consommation_brute_electricite_rte']),"normer"])
meteo_conso = res.execute(meteo_rg)
#print(meteo_conso.donnees[0:20])
#print(len(meteo_conso.donnees))