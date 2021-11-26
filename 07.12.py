shoppinglist = ["Mleko","Herbata","Kawa"]
y = input(f'podaj nazwe produktu: ')
file = open("shopping.txt", "a")
for x in shoppinglist:
    file.write(x)
    file.write("\n")
file.write(y)
file.write("\n")
file.close()

