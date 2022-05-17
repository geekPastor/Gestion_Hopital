"""définition de fonction Enregistrer un docteur : nom, prenom, postnom, téléphone
, matricule, spécialisation (ex: pédiatre, gynecologue, etc.)"""
Docteurs = []
def Enregistre_docteur():
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
     reponse = input("Voulez-vous ajouter un horaire pour ce Docteur? ")
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
    if len(Docteurs) > 0:
        for i in range(len(Docteurs)):
            print(f'Prénom : {Docteurs[i][0]}\nNom: {Docteurs[i][1]}\nPostnom: {Docteurs[i][2]}\nSpécialité : {Docteurs[i][3]}\nNuméro de téléphone : {Docteurs[i][4]}\nMatricule : {Docteurs[i][5]}\nGenre : {Docteurs[i][6]}')
    else :
        print("La liste est encore vide !")


def ajouter_horaire():
    choixUser = input("Vous voulez ajouter ou changer l'horaire: ")
    if choixUser.lower() == "ajouter":
        nomDocteur = input("Entrez le nom du docteur pour lequel vous voulez ajouter une tâche à l'horaire: ")
        for i in range(len(Docteurs)):
            if nomDocteur in Docteurs:
                choixuser = input("Ajouter à l'horaire  de combien des jours(1, 2, 3, 4, 5, 6, 7 ou tous): ")
                
                #pour ajouter l'horaire d'un jours
                
                if choixuser.lower() == "1":
                    
                    #pour savoir si l'hopital ouvre les portes chaque jour
                    choixJour = input("Vous travaillez tous les jours(même le dimanche): ")
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
                            print("Ce jour n'existe pas !!")
                            
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
                            
                #pour ajouter à l'horaire de deux jours
                elif choixuser.lower() == "2":
                    jour1 = input("Entrez le premier jour pour lequel vous voulez ajouter la tâche: ")
                    jour2 = input("Entrez le deuxième jour pour lequel vous voulez ajouter la tâche: ")
                    
                    #tester le cas où par erreur on tape la même chose les deux jours
                    while jour1 == jour2:
                        print("Attention ! les deux jours doivent être différents")
                        jour1 = input("Entrez le premier jour pour lequel vous voulez ajouter la tâche: ")
                        jour2 = input("Entrez le deuxième jour pour lequel vous voulez ajouter la tâche: ")
                        if jour1 != jour2:
                            break
                        else:
                            continue
                    #le cas où le deux jours sont différent

                    #pour le lundi et le mardi
                    if jour1.lower() == "lundi" and jour2.lower == "mardi":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du mardi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][8].append(action2)

                    #pour le lundi et le mercredi
                    elif jour1.lower() == "lundi" and jour2.lower == "mercredi":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du mercredi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][9].append(action2)

                    #pour le lundi et le jeudi  
                    elif jour1.lower() == "lundi" and jour2.lower == "jeudi":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du jeudi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][10].append(action2)

                    #pour le lundi et le vendredi
                    elif jour1.lower() == "lundi" and jour2.lower == "vendredi":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du vendredi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][11].append(action2)

                    #pour le lundi et le samedi
                    elif jour1.lower() == "lundi" and jour2.lower == "samedi":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][12].append(action2)

                    #pour le lundi et le dimanche
                    elif jour1.lower() == "lundi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du lundi: ")
                        action2 = input("Entrez la tâche du vendredi: ")
                        Docteurs[i][7].append(action1)
                        Docteurs[i][13].append(action2)

                    #pour le mardi et le mercredi
                    elif jour1.lower() == "mardi" and jour2.lower == "mercredi":
                        action1 = input("Entrez la tâche du mardi: ")
                        action2 = input("Entrez la tâche du mercredi: ")
                        Docteurs[i][8].append(action1)
                        Docteurs[i][9].append(action2)

                    #pour le mardi et le jeudi
                    elif jour1.lower() == "mardi" and jour2.lower == "jeudi":
                        action1 = input("Entrez la tâche du mardi: ")
                        action2 = input("Entrez la tâche du jeudi: ")
                        Docteurs[i][8].append(action1)
                        Docteurs[i][10].append(action2)

                    #pour le mardi et le vendredi
                    elif jour1.lower() == "mardi" and jour2.lower == "vendredi":
                        action1 = input("Entrez la tâche du mardi: ")
                        action2 = input("Entrez la tâche du vendredi: ")
                        Docteurs[i][8].append(action1)
                        Docteurs[i][11].append(action2)

                    #pour le mardi et le samedi
                    elif jour1.lower() == "mardi" and jour2.lower == "samedi":
                        action1 = input("Entrez la tâche du mardi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][8].append(action1)
                        Docteurs[i][12].append(action2)

                    #pour le mardi et le dimanche
                    elif jour1.lower() == "mardi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du mardi: ")
                        action2 = input("Entrez la tâche du dimanche: ")
                        Docteurs[i][8].append(action1)
                        Docteurs[i][13].append(action2)

                    #pour le mercredi et jeudi
                    elif jour1.lower() == "mercredi" and jour2.lower == "jeudi":
                        action1 = input("Entrez la tâche du mercredi: ")
                        action2 = input("Entrez la tâche du jeudi: ")
                        Docteurs[i][9].append(action1)
                        Docteurs[i][10].append(action2)
                        
                    #pour le mercredi et vendredi
                    elif jour1.lower() == "mercredi" and jour2.lower == "vendredi":
                        action1 = input("Entrez la tâche du mercredi: ")
                        action2 = input("Entrez la tâche du vendredi: ")
                        Docteurs[i][9].append(action1)
                        Docteurs[i][11].append(action2)

                    #pour le mercredi et samedi
                    elif jour1.lower() == "mercredi" and jour2.lower == "samedi":
                        action1 = input("Entrez la tâche du mercredi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][9].append(action1)
                        Docteurs[i][12].append(action2)

                    #pour le mercredi et dimanche
                    elif jour1.lower() == "mercredi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du mercredi: ")
                        action2 = input("Entrez la tâche du jeudi: ")
                        Docteurs[i][9].append(action1)
                        Docteurs[i][13].append(action2)

                    #pour le jeudi et vendredi
                    elif jour1.lower() == "jeudi" and jour2.lower == "vendredi":
                        action1 = input("Entrez la tâche du jeudi: ")
                        action2 = input("Entrez la tâche du vandredi: ")
                        Docteurs[i][10].append(action1)
                        Docteurs[i][11].append(action2)

                    #pour le jeudi et le samedi
                    elif jour1.lower() == "jeudi" and jour2.lower == "samedi":
                        action1 = input("Entrez la tâche du jeudi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][10].append(action1)
                        Docteurs[i][12].append(action2)

                    #pour le jeudi et dimanche
                    elif jour1.lower() == "jeudi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du jeudi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][10].append(action1)
                        Docteurs[i][13].append(action2)

                    #pour le vendredi et le samedi
                    elif jour1.lower() == "vendredi" and jour2.lower == "samedi":
                        action1 = input("Entrez la tâche du vendredi: ")
                        action2 = input("Entrez la tâche du samedi: ")
                        Docteurs[i][11].append(action1)
                        Docteurs[i][12].append(action2)

                    #pour le vendredi et dimanche
                    elif jour1.lower() == "vendredi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du vendredi: ")
                        action2 = input("Entrez la tâche du dimanche: ")
                        Docteurs[i][11].append(action1)
                        Docteurs[i][13].append(action2)

                    #pour le samedi et le dimanche
                    elif jour1.lower() == "samedi" and jour2.lower == "dimanche":
                        action1 = input("Entrez la tâche du samedi: ")
                        action2 = input("Entrez la tâche du dimanche: ")
                        Docteurs[i][12].append(action1)
                        Docteurs[i][13].append(action2)

                    else:
                        print("Ces jours n'existent pas !")
                #pour le cas où on choisit trois jours
                elif choixuser.lower() == "3":
                    jour1 = input("Entrez le premier jour pour lequel vous voulez ajouter la tâche: ")
                    jour2 = input("Entrez le deuxième jour pour lequel vous voulez ajouter la tâche: ")
                    jour3 = input("Entrez le troisième jour pour lequel vous voulez ajouter la tâche: ")

                    #pour le lundi, mardi et mercerdi
                    if jour1 == "lundi" and jour2 == "mardi" and jour3 == "mercredi":
                        
                elif choixuser.lower() == "Tous":
                    travail = input("Travaillez-vous aussi le dimanche(oui ou non): ")
                    if travail.lower() == "non"
                        lundi = input("Ajouter quelques chose à l'horaire du lundi: ")
                        mardi = input("Ajouter quelques chose à l'horaire du mardi: ")
                        mercredi = input("Ajouter quelques chose à l'horaire du mercredi: ")
                        jeudi = input("Ajouter quelques chose à l'horaire du jeudi: ")
                        vendredi = input("Ajouter quelques chose à l'horaire du vendredi: ")
                        samedi = input("Ajouter quelques chose à l'horaire du samedi: ")
                        Docteurs[i][7].append(lundi)
                        Docteurs[i][8].append(mardi)
                        Docteurs[i][9].append(mercredi)
                        Docteurs[i][10].append(jeudi)
                        Docteurs[i][11].append(vendredi)
                        Docteurs[i][12].append(samedi)
                    elif travail.lower == "oui":
                        lundi = input("Ajouter quelques chose à l'horaire du lundi: ")
                        mardi = input("Ajouter quelques chose à l'horaire du mardi: ")
                        mercredi = input("Ajouter quelques chose à l'horaire du mercredi: ")
                        jeudi = input("Ajouter quelques chose à l'horaire du jeudi: ")
                        vendredi = input("Ajouter quelques chose à l'horaire du vendredi: ")
                        samedi = input("Ajouter quelques chose à l'horaire du samedi: ")
                       dimanche = input("Ajouter quelques chose à l'horaire du dimanche: ")
                       Docteurs[i][7].append(lundi)
                       Docteurs[i][8].append(mardi)
                       Docteurs[i][9].append(mercredi)
                       Docteurs[i][10].append(jeudi)
                       Docteurs[i][11].append(vendredi)
                       Docteurs[i][12].append(samedi)
                       Docteurs[i][13].append(dimanche)
