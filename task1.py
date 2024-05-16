n = int(input())
a = "salom.txt"

with open(a, "r") as file:
    lines = file.readlines()

for line in lines[-n:]:
    print(line, end='')
