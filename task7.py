import random

with open("salom.txt", "r") as file:
    line = file.readlines()
    num = random.choice(line)
    n = num.strip()
    print(n)
