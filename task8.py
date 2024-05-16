with open('salom.txt', 'r') as file:


    num = file.read()
    new_line = num.replace('\n', '')
    print(new_line)
