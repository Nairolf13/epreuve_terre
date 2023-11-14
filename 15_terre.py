import sys 

if len(sys.argv) <= 1 or sys.argv[1].isalpha():
    print("Erreur !")
    sys.exit(1)

liste = []

for c in sys.argv [1:]:
    nombre = int(c)
    liste += [nombre]

est_triéé = True

for i in range (len(liste)-1):
    if liste[i] > liste [i+1]:
        est_triéé = False
        break
if est_triéé:
    print("La liste est triée !")
else:
    print("La liste n'est pas triée !")
