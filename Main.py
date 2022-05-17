#le début du programme


#Importation des différentes fonction
from Patients import Enregistre_patient, chercher_patient_avec_numero_dossier, Afficher_patient, Afficher_les_plaintes_patient, Afficher_imc_patient, chercher_patient_avec_ses_identifiants
from Docteur import Enregistre_docteur, Afficher_docteur
print("################################################################")
print("##                                                            ##")
print("##         PROGRAMME DE GESTION D'UN HOPITAL EN PYTHON        ##")
print("##                                                            ##")
print("################################################################")

#La déclaration des variables globales




def fonction_principale():
    choix = input("\n\nVoici les actions que vous pouvez éffectuer dans ce programme :\nA Pour ajouter et enregistre un docteur\nB Pour Enregistrer un patient\nC Pour Chercher un patient par ses identités\nD Chercher un patient par le numero de dossier\nE Pour Afficher tous les patients\nF Pour Afficher tous les docteurs\nG Afficher les plaintes d'un patient à partir de son numero unique\nH Pour Afficher l'IMC (indice de masse corporel) d'un patient\nI Pour quitter le programme\nQue voulez-vous faire >>>>")
    if choix.lower() == "i":
        exit()
    elif choix.lower() == "a":
        Enregistre_docteur()
        fonction_principale()
    elif choix.lower() == "b":
        Enregistre_patient()
        fonction_principale()
    elif choix.lower() == "c":
        chercher_patient_avec_ses_identifiants()
        fonction_principale()
    elif choix.lower() == "d":
        chercher_patient_avec_numero_dossier()
        fonction_principale()
    elif choix.lower() == "e":
        Afficher_patient()
        fonction_principale()
    elif choix.lower() == "f":
        Afficher_docteur()
        fonction_principale()
    elif choix.lower() == "g":
        Afficher_les_plaintes_patient()
        fonction_principale()
    elif choix.lower() == "h":
        Afficher_imc_patient()
        fonction_principale()
    else :
        print("Cette fonction n'est pas reconnu !\n\n")
        fonction_principale()
fonction_principale()
