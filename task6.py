a = ['home', 'work', 'khuna ', 'in list hast bud shud']
add_to_list = 'salom.txt'

with open(add_to_list, 'w') as file:
    for item in a:
        file.write(item + '\n')

print(add_to_list)






