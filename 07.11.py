film_tiltes = ["Bob Budowniczy","Muminki","Władca pierscieni","Fantastyczne Zwierzeta","Power"]

file = open("films.txt", "w")
for x in film_tiltes:
    file.write(x)
    file.write("\n")
file.close()