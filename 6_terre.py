import sys 


nombre1 = int(sys.argv[1])
nombre2 = int(sys.argv[2])

try:
    if nombre1 < nombre2:
        print("Erreur")
    else:
        resultat = int(nombre1) // int(nombre2)  
        reste = int(nombre1) % int(nombre2)
        print(resultat)
        print(reste)

except ZeroDivisionError:
    print("Ne pas diviser pas zero !")