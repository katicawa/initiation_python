import random
liste = ["carotte" , "turpitude" , "ardoise"]
solution = random.choice(liste)
tentatives = 7
affichage = ""

for l in solution :
    affichage = affichage + "_ "

lettres_trouvees = ""
while tentatives > 0 :
    print("mot a deviner : \n", affichage)
    proposition = input("proposez une lettre : \n")
    if proposition in solution :
        lettres_trouvees = lettres_trouvees + proposition
        print("Bien vu !")

    else :
        tentatives = tentatives - 1
        print("Dommage ! Il vous reste", tentatives , "tentatives \n")
        if tentatives == 0 :
            print("==========Y= ")
        if tentatives <= 1 :
            print(" ||/       |  ") 
        if tentatives <= 2 :
            print(" ||        0  ")
        if tentatives <= 3 :
            print(" ||       /|\ ")
        if tentatives <= 4 :
            print(" ||       /|  ")
        if tentatives <= 5 :
            print("/||           ")
        if tentatives <= 6 :
            print("==============\n")
        if tentatives == 0 :
            print("Vous avez perdu !")

    affichage = ""
    for x in solution :
        if x in lettres_trouvees :
            affichage += x + " "
        else :
            affichage += "_ "
    if "_" not in affichage : 
        print("C'est gagné !\n" , solution)
        break