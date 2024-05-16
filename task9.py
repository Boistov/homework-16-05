name = "salom.txt"

with open(name) as n:
    a = n.read()
    a = a.replace(",", " ")
    word = len(a.split())
    print(name, word)
