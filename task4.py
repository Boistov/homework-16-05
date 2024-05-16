nom = 'salom.txt'

with open(nom, 'r') as file:
    lines = len(file.readlines())
    print('Total Number of lines:', lines)
