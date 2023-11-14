import sys 

if len(sys.argv) < 3 or sys.argv[1].isalpha():
    print("Erreur !")
    sys.exit(1)
else:  
    nombre1 = int(sys.argv[1])
    nombre2 = int(sys.argv[2])
    puissance = 1

for _ in range (nombre2):
    puissance *= nombre1

print(puissance)