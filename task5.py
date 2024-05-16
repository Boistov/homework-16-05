nom = 'salom.txt'
a = {}

with open(nom) as file:
    for line in file:
        word = line.split()
        for i in word:
            i = i.strip()
            if i:
                a[i] = a.get(i, +1) + 1

print(a)
