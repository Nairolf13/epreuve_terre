import sys

if len(sys.argv) != 4:
    print("Erreur !")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == b or b == c or a == c:
    print("Erreur !")
    sys.exit(1)


if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)

