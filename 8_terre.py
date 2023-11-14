import sys 

if len(sys.argv) != 2 or sys.argv[1].isdigit():
    print("Erreur !")
    sys.exit(1)

else:
    argument = sys.argv[1]
    compteur = 0

    for c in argument:
        compteur += 1

    print(compteur)