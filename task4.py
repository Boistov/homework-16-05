nom = 'salom.txt'

with open(nom, 'r') as file:
    line = len(file.readlines())
    print(line)
