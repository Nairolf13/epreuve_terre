import sys 

heures_24 = sys.argv[1:]

if len(sys.argv) <= 1:
    print("Erreur !")
    sys.exit(1)

heure = heures_24[0][:2]
minute = heures_24[0][-2:]
fin = ""
heure_12 = int(heure)

if int(heure) > 12:
    heure_12 = int(heure) - 12 

if int(heure) >= 12:
    fin = "PM"

    print(f"{heure_12}:{minute}{fin}")

else:
    fin = "AM"

    print(f"{heure}:{minute}{fin}")

