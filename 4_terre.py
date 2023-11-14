import sys 

argument = sys.argv [1]

for lettre in range(ord(argument), ord("z")+1):
    
    print(chr(lettre), end="")

print()