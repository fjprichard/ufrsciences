# ufrsciences
Outils d'analyse des formations (UFR sciences AMU)

Ce programme s'adresse aux directeurs des départements de l'UFR sciences d'AMU. Il permet d'analyser les offres de formation au sein d'un UFR. Il repose sur des extraction de l'application GDEP.

# Mode d'emploi.
 
 - Recueil des données dans GDEP:
        - aller dans l'onglet synthese
        - cliquer sur exporter,
        - sauvergarder le fichier au format xlsx (fichier "nom_fichier.xlsx")
 - Dans python,
        - si nécessaire, installer la librairie pandas,
        - editer analyse.py,
        - renseigner l'adresse physique du fichier en le mettant dans 
          chemin_donnees = "nom_fichier.xlsx"
        - exécuter le programme. 
        - le programme affiche le nombre d'heures affectées à des enseignants par formation.
        

        

