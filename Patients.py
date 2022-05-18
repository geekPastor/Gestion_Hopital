import os
from Clear_consol import clear_consol

""" Enregistrer un patient : nom, prenom, postnom, téléphone
, poids, taille, genre, age, numero de dossier (un code unique que vous allez généré)"""


Patients = []
def Enregistre_patient():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    ENREGISTRER UN PATIENT                  ##")
    print("##                                                            ##")
    print("################################################################")
    identites_patient= []
    imc = ""
    prenom_patient = input("Entrez le prenom du patient: ")
    nom_patient = input("Entrez le nom du patient: ")
    postnom_patient = input("Entrez le postenom du patient: ")
    tel_patient = input("Entrez le numéro de téléphone du patient: ")
    poids_patient = float(input("Entrez le poids du patient"))
    taille_patient = float(input("Entrez la taille du patient: "))
    genre_patient = input("Entrez le genre du nouveau patient M ou F: ")
    age_patient = int(input("Entrez l'âge du patient: "))
    plaintes_patient = input("De quoi souffre le patient: ")
    date = input("Entrez la date du jours avec cette anneautation 22-06-2022: ")
    indice_de_masse_corporel_patient = poids_patient / taille_patient
    if indice_de_masse_corporel_patient < 18.5:
        imc = "Insuffisance pondérale (maigreur)"
    elif indice_de_masse_corporel_patient >= 18.5 and indice_de_masse_corporel_patient < 25:
        imc = "Corpulence normale"
    elif indice_de_masse_corporel_patient >= 25 and indice_de_masse_corporel_patient < 30:
        imc = "Surpoids"
    elif indice_de_masse_corporel_patient >= 30 and indice_de_masse_corporel_patient < 35:
        imc = "Obésité modérée"
    elif indice_de_masse_corporel_patient >= 35 and indice_de_masse_corporel_patient < 40:
        imc = "Obésité sévère"
    elif indice_de_masse_corporel_patient > 40:
        imc = "Obésité morbide ou massive"
    numero_dossier_patient = str(id)+str(date[0:2])+str(nom_patient[0].upper())+str(date[3:5])+str(postnom_patient[0].upper())+str(date[7::])
    identites_patient.append(prenom_patient.upper())
    identites_patient.append(nom_patient.upper())
    identites_patient.append(postnom_patient.upper())
    identites_patient.append(poids_patient)
    identites_patient.append(taille_patient)
    identites_patient.append(genre_patient.upper())
    identites_patient.append(age_patient)
    identites_patient.append(imc.upper())
    identites_patient.append(plaintes_patient.upper())
    identites_patient.append(numero_dossier_patient)
    identites_patient.append(date)
    identites_patient.append(tel_patient)
    Patients.append(identites_patient)


    
"""Chercher un patient par le numero de dossier
et on retourne le seul patient ayant ce numero """

def chercher_patient_avec_numero_dossier():
    clear_consol()s
    numero_dossier = int(input("Entrez le numéro du dossier du patient: "))
    for i in range(len(Patients)):
        for j in Patients[i]:
            if numero_dossier == Patients[i][-3]:
                print(Patients[i])
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")



"""Afficher tous les patients"""
def Afficher_patient():
    clear_consol()
    if len(Patients) > 0:
        for i in range(len(Patients)):
            print(f'Prénom : {Patients[i][0]}\nNom: {Patients[i][1]}\n Postnom: {Patients[i][2]}\nNuméro de téléphone du patient :{Patients[i][-1]}\nPoids : {Patients[i][3]}\nTaille : {Patients[i][4]}\nGenre : {Patients[i][5]}\nAge : {Patients[i][6]}\nIMC : {Patients[i][7]}\nPlaintes : {Patients[i][8]}\nNuméro du dossier :{Patients[i][9]}\nDate : {Patients[i][10]}')
    else :
        print("La liste est encore vide !")


"""Afficher les plaintes d'un patient à partir de son numero unique"""

def Afficher_les_plaintes_patient():
    clear_consol()
    numero_dossier = int(input("Entrez le numéro du dossier du patient: "))
    for i in range(len(Patients)):
        for j in Patients[i]:
            if numero_dossier == Patients[i][-3]:
                print(Patients[i][-4])
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")

                
def Afficher_imc_patient():
    clear_consol()
    numero_dossier = int(input("Entrez le numéro du dossier du patient: "))
    for i in range(len(Patients)):
        for j in Patients[i]:
            if numero_dossier == Patients[i][-3]:
                print(Patients[i][-5])
                break
            else :
                print("Aucun patuient n'a ce numéro dans la liste")



"""Chercher un patient par ses identités (nom, postnom ou prénom)
et on nous retourne la liste des utilisateurs ayants ces informations """

def chercher_patient_avec_ses_identifiants():
    clear_consol()
    chercher_patient = []
    nom = input("Entrez le nom du patient que vous voulez chercher: ")
    postnom = input("Entrez le postnom du patient que vous voulez chercher: ")
    prenom = input("Entrez le prenom du patient que vous voulez chercher: ")
    chercher_patient.append(nom)
    chercher_patient.append(postnom)
    chercher_patient.append(prenom)
    for i in range(len(Patients)):
        if chercher_patient in Patients:
            print(f'Prénom : {Patients[i][0]}\nNom: {Patients[i][1]}\n Postnom: {Patients[i][2]}\nPoids : {Patients[i][3]}\nTaille : {Patients[i][4]}\nGenre : {Patients[i][5]}\nAge : {Patients[i][6]}\nIMC : {Patients[i][7]}\nPlaintes : {Patients[i][8]}\nNuméro du dossier :{Patients[i][9]}\nDate : {Patients[i][10]}')
        else :
            print("Ses identifiants ne sont pas dans la liste des patients")
