import random
print("Rentrer borne inférieure \n")
a = int(input())
print("Rentrer borne supérieure \n")
b = int(input())

juste_prix = random.randint(a, b)
found = False
print("Bienvenue au juste prix ! Veuillez choisir un nombre \n")

while (not found):
    proposition = int(input())
    if proposition < juste_prix :
        print("C'est plus \n")
    elif proposition > juste_prix :
        print("Cest moins \n")
    else :
        found = True
print("C'est gagné ! \n")