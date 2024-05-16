with open("salom.txt", "r") as file:
    a = file.readlines()
    a = [line.strip() for line in a]
    print(a)
