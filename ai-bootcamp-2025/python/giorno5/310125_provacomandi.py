name = "pippo.txt"
fd2 = open("name", "w")
fd2.write("Ciao!")
fd2.close()
fd2 = open("name", "r")
print(fd2.read())
fd2.close()

with open(name, "r") as fd3:
    print(fd3.read())

text = None
while text is None:
    text = input("Nome?")
print(f"Il tuo nome è {text}")

text = ""
while text := "":
    text = input(">>>")
    print(f"Il tuo nome è {text}")