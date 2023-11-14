import sys 

resultat = sys.argv[1]
nombre = int(resultat)

if nombre % 2 != 0:
 print(f"{resultat} est impaire")
else:
 print(f"{resultat} est pair")