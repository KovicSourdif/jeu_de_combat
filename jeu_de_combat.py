import random
import os

play = True
niveau_vie = 20
choix = 0
force_adversaire = 0
force_usager = 0
afficher_menu = True
numero_adv = 1
nb_combat = 1
nb_victoire = 0
nb_defaite = 0
victoire_consecutive = 0


def genere_adv ():
    global force_adversaire
    numero_adv =+ 1
    force_adversaire =  random.randint(1,5)
    print('\033[1;33mVous tombez face à face avec un adversaire de difficulté : ' + str(force_adversaire) + '\n')

def menu():
    global afficher_menu
    global choix

    while afficher_menu:

        choix = int(input("\033[1;97mQue voulez-vous faire ? \n 1- Combattre cet adversaire \n 2- Contourner cet adversaire et aller ouvrir une autre porten \n 3- Afficher les règles du jeu \n 4- Quitter la partie \n"))
        if choix == 1:

            afficher_menu = False


        if choix == 2:
            afficher_menu = False

        if choix == 3:
            print("\033[1;34m\n Pour réusir un combat , il faut que la valeur du dé lancé soit \n supérieure à la force de l'adversaire. Dans ce cas, le niveau \n de vie de l'usager est augmenté de la force de l'adversaire.\n Une défaite a lieu lorsque la valeur du dé lancé par l'usager \n est inférieure ou égale à la fore de l'adversaire. Dans ce \n cas, le niveau de vie de l'usager est diminué de la force de \n l'adversaire. \n \n L'usager peut combattre ou éviter chaque adversaire, dans le \n cas de l'évitement, il y a une pénaltié de 1 point de vie.\n\n\n\033[1;97m")
        if choix == 4:
            afficher_menu = False
    afficher_menu = True


    return choix
def combat():
    pass

while play:
    genere_adv()
    action = menu()

    if action == 1:
        print('Adversaire : ' + str(numero_adv))
        print("Force de l'advesaire : " + str(force_adversaire))
        print("Niveau de vie de l'usager :" + str(niveau_vie))
        print("Combat " + str(nb_combat) + ":" + str(nb_victoire) + " VS " + str(nb_defaite))

        force_usager = random.randint(1, 6)
        print('Lancer du dé : ' + str(force_usager))
        if force_usager > force_adversaire:
            niveau_vie += force_adversaire
            nb_combat += 1
            nb_victoire += 1
            victoire_consecutive +=1
            print('Dernier combat = Victoire')
            print("Niveau de vie : " + str(niveau_vie))
            print("Nombre vicoitres consécutives : " + str(victoire_consecutive))

        else:
            niveau_vie -= force_adversaire
            nb_combat += 1
            nb_defaite += 1
            victoire_consecutive = 0
            print('Dernier combat = Défaite')
            print('Niveau de vie : ' + str(niveau_vie))
            if niveau_vie < 1:
                print('La partie est terminée, vous avez vaicu ' + str(nb_victoire) + ' monstres')
    if action == 2:
        niveau_vie -= 1

    if niveau_vie <= 0:
        print('La partie est terminée, vous avez vaincu ' + str(nb_victoire) + 'monstre(s).')
        print("Recréation d'une nouvelle partie")
        niveau_vie = 20
        nb_victoire = 0
        numero_adv = 1
        nb_defaite = 0
        nb_combat = 1
