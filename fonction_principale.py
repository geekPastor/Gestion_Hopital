#le début du programme
import os
from Clear_consol import clear_consol
from Patients import Enregistre_patient, chercher_patient_avec_numero_dossier, Afficher_patient, Afficher_les_plaintes_patient, Afficher_imc_patient, chercher_patient_avec_ses_identifiants
from Docteur import Enregistre_docteur,  Afficher_docteur, ajouter_ou_changer_horaire,  Afficher_horaire,  Enregistrer_horaire
print("################################################################")
print("##                                                            ##")
print("##         PROGRAMME DE GESTION D'UN HOPITAL EN PYTHON        ##")
print("##                                                            ##")
print("################################################################")

#La déclaration des variables globales




def fonction_principale():
    choix = input(f'Voici les actions que vous pouvez réaliser dans ce programme\n1: Pour Enregistrer un docteur\n2: Pour Enregistrer un patient\n3: Chercher un patient par ses identités\n4: Chercher un patient par le numero de dossier\n5: Afficher tous les patients\n6: Afficher tous les docteurs\n7: Enregistrer l\'horaire de chaque medecin\n8: Afficher les plaintes d\'un patient à partir de son numero unique\n9: Afficher l\'IMC (indice de masse corporel) d\'un patient\n10: Pour quitter le programme')
    if choix.lower() == "10":
        exit()
        
    elif choix.lower() == "1":
        Enregistre_docteur()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "2":
        Enregistre_patient()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "3":
        chercher_patient_avec_ses_identifiants()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "4":
        chercher_patient_avec_numero_dossier()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "5":
        Afficher_patient()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "6":
        Afficher_docteur()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "7":
        Enregistrer_horaire
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "8":
        Afficher_les_plaintes_patient()
        os.system('pause')
        clear_consol()
        fonction_principale()
        
    elif choix.lower() == "9":
        Afficher_imc_patient()
        os.system('pause')
        clear_consol()
        fonction_principale()
    else :
        print("Cette fonction n'est pas reconnu !\n\n")
        os.system('pause')
        clear_consol()
        fonction_principale()
fonction_principale()
