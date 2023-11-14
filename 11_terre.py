import sys 

def prime_number(nombre):

    if nombre <= 1:
        return ("0 et 1 ne sont pas des nombres premiers ")
    
    for n in range (2, int(nombre**0.5) + 1):
        if nombre % n == 0:
            return (f"{nombre} n'est pas premier !")
    return (f"{nombre} est premier !")


if len(sys.argv) <= 1 or sys.argv[1].isalpha():
    print("Erreur !")
    sys.exit(1)

nombre = int(sys.argv[1])
resultat = prime_number(nombre)  

print(resultat)