# -*- coding: utf-8 -*-
"""
Analyse des heures de formation dans les départements de l'UFR Sciences à AMU.
Auteur: Frédéric Richard, 2023.

Note: ce programme nécessite l'installation préalable de la librairie pandas.
"""
import pandas as pd

chemin_donnees = "../2022-23/synthese-math-2023-02-22.xlsx"


def MiseEnFormeDesDonnees(df):
    """Met en forme les données issues de l'extraction de GDEP.

    Pour extraire le fichier brut dans gdep:
        - aller dans l'onglet synthese
        - cliquer sur exporter,
        - sauvergarder le fichier au format xlsx.

    Paramètres
    ----------
    df : DataFrame
        Données importées du fichier xlsx avec pandas.


    Sortie
    ------
    DataFrame : données mises en forme
        variables du tableau:
            - 'Nom': nom de l'enseignant
            - 'Statut': statut de l'enseignant
            - 'Cycle': cycle de formation
            - 'Formation': formation
            - 'Parcours': parcours
            - 'Site': site
            - 'Année': année
            - 'Type ': type d'enseignenement.
            - 'Heures': nombre d'heures enseignées (en eq TD).
    """
    info = []
    for x in df.itertuples():
        if isinstance(x._1, str):
            # Recherche des informations sur la formation.
            j = x._1.find(" - ")
            if j > 0:
                formation = x._1[0: j]
                aux = x._1[j+2:]
                j = aux.find(" - ")
                if j > 0:
                    parcours = aux[0: j]
                    aux = aux[j+2:]
                    j = aux.find("S")
                    if j > 0:
                        semestre = aux[j+1]
                        if semestre == "1" or semestre == "2":
                            annee = 1
                        elif semestre == "3" or semestre == "4":
                            annee = 2
                        elif semestre == "5" or semestre == "6":
                            annee = 3
                    else:
                        semestre = ""
                        annee = 0
                else:
                    parcours = ""
                    semestre = ""
                    annee = 0
            else:
                formation = x._1
                parcours = ""
                semestre = ""
                annee = 0

            if "Master" in formation:
                cycle = "2e cycle"
            else:
                cycle = "1er cycle"

        if isinstance(x._2, str):
            # Recherche des informations sur l'enseignement.
            j = x._2.find(" - ")
            if j > 0:
                aux = x._2[j+2:]
                while j > 0:
                    j = aux.find(" - ")
                    aux = aux[j+2:]
                site = aux

        if isinstance(x._11, str):
            # Recherche d'heures affectées à un enseignant.
            if x._11 == "A":
                if isinstance(x._3, str):
                    # Recherche des informations sur l'enseignant.
                    j = x._3.find("(")
                    nom = x._3[0:j]
                    aux = x._3[j+1:]
                    j = aux.find(")")
                    statut = aux[0:j]
                    j = statut.find(" ")
                    if j > 0:
                        statut = statut[0: j]

                    if isinstance(x._6, str):
                        j = x._6.find(" h")
                        cm = float(x._6[0: j])
                    else:
                        cm = 0
                    if isinstance(x._7, str):
                        j = x._7.find(" h")
                        td = float(x._7[0: j])
                    else:
                        td = 0
                    if isinstance(x._8, str):
                        j = x._8.find(" h")
                        tp = float(x._8[0: j])
                    else:
                        tp = 0
                    if isinstance(x._9, str):
                        j = x._9.find(" h")
                        pa = float(x._9[0: j])
                    else:
                        pa = 0

                    # Sauvegarde des informations.
                    if cm != 0:
                        info.append([nom, statut,
                                     cycle, formation, parcours, site, annee,
                                     "CM", cm * 1.5])
                    if td != 0:
                        info.append([nom, statut,
                                     cycle, formation, parcours, site, annee,
                                     "TD", td])
                    if tp != 0:
                        info.append([nom, statut,
                                     cycle, formation, parcours, site, annee,
                                     "TP", tp])
                    if pa != 0:
                        info.append([nom, statut,
                                     cycle, formation, parcours, site, annee,
                                     "PA", pa])

    df = pd.DataFrame(info, columns=['Nom', 'Statut',
                                     'Cycle', 'Formation', 'Parcours',
                                     'Site', 'Année', 'Type', 'Heures'])

    return(df)


# Importation et mise en forme des données.
df = pd.read_excel(chemin_donnees)
df = MiseEnFormeDesDonnees(df)

# Calcul des heures affectées par formation.
of = df.groupby(by=['Cycle', 'Formation'])['Heures'].sum().to_frame()
print(of)
