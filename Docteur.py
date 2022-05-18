import os
from Clear_consol import clear_consol


"""définition de fonction Enregistrer un docteur : nom, prenom, postnom, téléphone
, matricule, spécialisation (ex: pédiatre, gynecologue, etc.)"""
Docteurs = []
def Enregistre_docteur():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    ENREGISTRER UN DOCTEURS                 ##")
    print("##                                                            ##")
    print("################################################################")
    identites_docteur= []
    prenom = input("Entrez le prenom du nouveau docteur: ")
    nom = input("Entrez le nom du nouveau docteur: ")
    postnom = input("Entrez le postenom du nouveau docteur: ")
    tel = input("Entrez le numéro de téléphone du nouveau docteur: ")
    specialisation = input("Quel est la spécialisattion du nouveau docteur: ")
    Genre= input("Entrez le genre du nouveau docteur (M ou F): ")
    matricule = nom[0]+postnom[0]+prenom[0:4]+tel[-1:-4:-1]
    identites_docteur.append(prenom)
    identites_docteur.append(nom)
    identites_docteur.append(postnom)
    identites_docteur.append(specialisation)
    identites_docteur.append(tel)
    identites_docteur.append(matricule)
    identites_docteur.append(Genre)
    reponse = input("Voulez-vous ajouter un horaire pour ce Docteur (oui ou non)? ")
     
    if reponse.lower() == "oui":
        travail = input("Travaillez-vous aussi le dimanche(oui ou non): ")
        
        if travail.lower() == "non":
            jour1 = input("Entrez son horaire du lundi: ")
            jour2 = input("Entrez son horaire du mardi: ")
            jour3 = input("Entrez son horaire du mercredi: ")
            jour4 = input("Entrez son horaire du jeudi: ")
            jour5 = input("Entrez son horaire du vendredi: ")
            jour6 = input("Entrez son horaire du samedi: ")
            identites_docteur.append(jour1)
            identites_docteur.append(jour2)
            identites_docteur.append(jour3)
            identites_docteur.append(jour4)
            identites_docteur.append(jour5)
            identites_docteur.append(jour6)
            
        elif travail.lower() == "oui":
            jour1 = input("Entrez son horaire du lundi: ")
            jour2 = input("Entrez son horaire du mardi: ")
            jour3 = input("Entrez son horaire du mercredi: ")
            jour4 = input("Entrez son horaire du jeudi: ")
            jour5 = input("Entrez son horaire du vendredi: ")
            jour6 = input("Entrez son horaire du samedi: ")
            jour7 = input("Entrez son horaire du dimanche: ")
            identites_docteur.append(jour1)
            identites_docteur.append(jour2)
            identites_docteur.append(jour3)
            identites_docteur.append(jour4)
            identites_docteur.append(jour5)
            identites_docteur.append(jour6)
            identites_docteur.append(jour7)
    elif reponse.lower() == "non":
        print("Okay vous pouvez ajouter plus tard !!")
    Docteurs.append(identites_docteur)


"""Afficher tous les docteurs"""
def Afficher_docteur():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    VOICI LA LISTE DE TOUS LES DOCTEURS                ##")
    print("##                                                            ##")
    print("################################################################")
    if len(Docteurs) > 0:
        for i in range(len(Docteurs)):
            print(f'Prénom : {Docteurs[i][0]}\nNom: {Docteurs[i][1]}\nPostnom: {Docteurs[i][2]}\nSpécialité : {Docteurs[i][3]}\nNuméro de téléphone : {Docteurs[i][4]}\nMatricule : {Docteurs[i][5]}\nGenre : {Docteurs[i][6]}')
    else :
        print("La liste est encore vide !")

def Afficher_horaire():
    clear_consol()
    chercher_patient = []
    nom = input("Entrez le nom du patient que vous voulez chercher: ")
    postnom = input("Entrez le postnom du patient que vous voulez chercher: ")
    prenom = input("Entrez le prenom du patient que vous voulez chercher: ")
    chercher_patient.append(nom)
    chercher_patient.append(postnom)
    chercher_patient.append(prenom)
    for i in range(len(Docteurs)):
        if chercher_patient in Docteurs:
            print(f'Prénom : {Docteurs[i][0]}\nNom: {Docteurs[i][1]}\nPostnom : {Docteurs[i][2]}\nVoici son horaire :\n     Lundi :{Docteurs[i][7]}\n       Mardi :{Docteurs[i][8]}\n       Mercredi :{Docteurs[i][9]}\n        Jeudi :{Docteurs[i][10]}\n      Vendredi :{Docteurs[i][11]}\n       Samedi{Docteurs[i][12]}\n       Dimanche :{Docteurs[i][13]}')
        else :
            print("Ses identifiants ne sont pas dans la liste des patients")

            
def Enregistrer_horaire():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    ENREGISTRER L'HORAIRE DU DOCTEUR               ##")
    print("##                                                            ##")
    print("################################################################")
    travail = input("Travaillez-vous aussi le dimanche(oui ou non): ")
    if travail.lower() == "non":
            jour1 = input("Entrez son horaire du lundi: ")
            jour2 = input("Entrez son horaire du mardi: ")
            jour3 = input("Entrez son horaire du mercredi: ")
            jour4 = input("Entrez son horaire du jeudi: ")
            jour5 = input("Entrez son horaire du vendredi: ")
            jour6 = input("Entrez son horaire du samedi: ")
            identites_docteur.append(jour1)
            identites_docteur.append(jour2)
            identites_docteur.append(jour3)
            identites_docteur.append(jour4)
            identites_docteur.append(jour5)
            identites_docteur.append(jour6)
            
    elif travail.lower() == "oui":
            jour1 = input("Entrez son horaire du lundi: ")
            jour2 = input("Entrez son horaire du mardi: ")
            jour3 = input("Entrez son horaire du mercredi: ")
            jour4 = input("Entrez son horaire du jeudi: ")
            jour5 = input("Entrez son horaire du vendredi: ")
            jour6 = input("Entrez son horaire du samedi: ")
            jour7 = input("Entrez son horaire du dimanche: ")
            identites_docteur.append(jour1)
            identites_docteur.append(jour2)
            identites_docteur.append(jour3)
            identites_docteur.append(jour4)
            identites_docteur.append(jour5)
            identites_docteur.append(jour6)
            identites_docteur.append(jour7)


def ajouter_ou_changer_horaire():
    clear_consol()
    if len(Docteur) > 6:
        choixUser = input("Vous voulez ajouter ou changer l'horaire: ")
        if choixUser.lower() == "ajouter":
            nomDocteur = input("Entrez le nom du docteur pour lequel vous voulez ajouter une tâche à l'horaire: ")
            for i in range(len(Docteurs)):
                if nomDocteur in Docteurs:
                    choixJour = input("L'hopital ouvre-t-il ses portes chaques jour?  ")
                    if choixJour.lower == "oui": 
                            jour = input("Pour quel jour vous voulez ajouter la tâche: ")
                            if jour.lower() == "lundi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][7].append(action)
                                
                            elif jour.lower() == "mardi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][8].append(action)
                                
                            elif jour.lower() == "mercredi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][9].append(action)
                                
                            elif jour.lower() == "jeudi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][10].append(action)
                                
                            elif jour.lower() == "vendredi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][11].append(action)
                                
                            elif jour.lower() == "samedi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][12].append(action)
                                
                            elif jour.lower() == "dimanche":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][13].append(action)
                                
                            else:
                                print("Le jour que vous avez saisi n'existe pas !!")
                                
                    #pour savoir si l'hopital n'ouvre les portes chaque jour
                    elif choixJour.lower == "non":
                            jour = input("Pour quel jour vous voulez ajouter la tâche: ")
                            
                            if jour.lower() == "lundi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][7].append(action)
                                
                            elif jour.lower() == "mardi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][8].append(action)
                                
                            elif jour.lower() == "mercredi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][9].append(action)
                                
                            elif jour.lower() == "jeudi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][10].append(action)
                                
                            elif jour.lower() == "vendredi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][11].append(action)
                                
                            elif jour.lower() == "samedi":
                                action = input("Entrez la tâche à ajouter: ")
                                Docteurs[i][12].append(action)
                                
                            else :
                                print("Le jour que vous avez saisi n'existe pas !!")  


        elif choixUser.lower() == "Changer":
            jour = input("Pour quel jour vous voulez changer la tâche: ")
            if jour.lower() == "lundi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][7].append(action)
                                
            elif jour.lower() == "mardi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][8].append(action)
                                
            elif jour.lower() == "mercredi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][9].append(action)
                                
            elif jour.lower() == "jeudi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][10].append(action)
                                
            elif jour.lower() == "vendredi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][11].append(action)
                                
            elif jour.lower() == "samedi":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][12].append(action)
                                
            elif jour.lower() == "dimanche":
                action = input("Entrez la nouvelle tâche: ")
                Docteurs[i][13].append(action)
                                
            else:
                print("Le jour que vous avez saisi n'existe pas !!")
                                
    #pour savoir si l'hopital n'ouvre les portes chaque jour
    elif choixJour.lower == "non":
        jour = input("Pour quel jour vous voulez changer la tâche: ")

        if jour.lower() == "lundi":
            action = input("Entrez la nouvelle tâcher: ")
            Docteurs[i][7].append(action)
                                
        elif jour.lower() == "mardi":
            action = input("Entrez la nouvelle tâche: ")
            Docteurs[i][8].append(action)
                                
        elif jour.lower() == "mercredi":
            action = input("Entrez la nouvelle tâche: ")
            Docteurs[i][9].append(action)
                                
        elif jour.lower() == "jeudi":
            action = input("Entrez la nouvelle tâche: ")
            Docteurs[i][10].append(action)
                                
        elif jour.lower() == "vendredi":
            action = input("Entrez la nouvelle tâche: ")
            Docteurs[i][11].append(action)
                                
        elif jour.lower() == "samedi":
            action = input("Entrez la nouvelle tâche: ")
            Docteurs[i][12].append(action)
                                
        else :
            print("Le jour que vous avez saisi n'existe pas !!")
    else:
        print("Il n'y a pas d'horaire enregistrer jusque là !!")
