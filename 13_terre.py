import sys 

if len(sys.argv) <= 1:
    print("Erreur !")
    sys.exit(1)

heure_12 = sys.argv[1]
heures = int(heure_12[0:2])

if "PM" in heure_12 and heures != 12:
    heures += 12
elif "AM" in heure_12 and heures == 12:
    heures = 0 

minutes = int(heure_12[3:5])

print(f"{heures}:{minutes}")
