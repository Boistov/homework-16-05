nom = "salom.txt"

with open(nom, 'r') as file:
    words = file.read().split()
    maximum = len(max(words, key=len))
    n = [i for i in words if len(i) == maximum]

print(n)

