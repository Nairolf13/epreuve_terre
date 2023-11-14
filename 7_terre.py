import sys 

if len(sys.argv) < 2:
    print("Erreur !")
    sys.exit(1)

else:
    chaine = sys.argv[1]
    chaine_inversé = ""

    for c in range (len(chaine)-1, -1, -1):
        chaine_inversé += chaine[c]

print(chaine_inversé)