import sys

if len(sys.argv) <= 1 or sys.argv[1].isalpha():
    print("Erreur")
    sys.exit(1)

x = 1.0
a = int(sys.argv[1])

while abs(x * x - a) > 1e-10:
    x = 0.5 * (x + a / x)


print(round(x))
