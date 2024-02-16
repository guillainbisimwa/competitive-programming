# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())

annuaire = {}
for _ in range(n):
    nom, numero = input().split()
    annuaire[nom] = numero
# Add a while loop
while True:
    try:
        recherche = input().strip()
        if recherche in annuaire:
            print(f"{recherche}={annuaire[recherche]}")
        else:
            print("Not found")
    except EOFError:
        break

