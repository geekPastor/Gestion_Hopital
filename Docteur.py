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
        
        if travail.lower() == "non"
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
    elif reponse.lower() = "non":
        print("Okay vous pouvez ajouter plus tard !!")
    Docteurs.append(identites_docteur)


"""Afficher tous les docteurs"""
def Afficher_docteur():
    clear_consol()
    if len(Docteurs) > 0:
        for i in range(len(Docteurs)):
            print(f'Prénom : {Docteurs[i][0]}\nNom: {Docteurs[i][1]}\nPostnom: {Docteurs[i][2]}\nSpécialité : {Docteurs[i][3]}\nNuméro de téléphone : {Docteurs[i][4]}\nMatricule : {Docteurs[i][5]}\nGenre : {Docteurs[i][6]}')
    else :
        print("La liste est encore vide !")

def Afficher_horaire():
    clear_consol()
    if len(Docteurs) > 0:
        for i in range(len(Docteurs)):
            print(f'Prénom : {Docteurs[i][0]}\nNom: {Docteurs[i][1]}\n Postnom: {Docteurs[i][2]}\n voici l\'horaire de ce Docteur\nLundi :{Docteurs[i][7]}\nMardi :{Docteurs[i][8]}\nMercredi :{Docteurs[i][9]}\nJeudi :{Docteurs[i][10]}\nVendredi :{Docteurs[i][11]}\nSamedi :{Docteurs[i][12]}\nDimanche :{Docteurs[i][13]}')
    else :
        print("La liste est encore vide !")

def Enregistrer_horaire():
    clear_consol()
    travail = input("Travaillez-vous aussi le dimanche(oui ou non): ")
    if travail.lower() == "non"
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
