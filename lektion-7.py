"""
for x in range(1, 20):
    print(x)
    if ((x * 4) - 2) == 38:
        print("svaret är: ", x)
        break
"""

"""
x = 0
while True:
    x = x + 1
    print(x)
    if ((x * 4) - 2) == 38:
        print("svaret är", x)
        break
"""
"""
x = 0
while ((x * 4) - 2) != 38:
    print(x)
    x = x + 1 
print("svaret är", x)
"""
"""
x = 0 
while x < 5:
    print("This number is:", x) 
    x = x + 1
    if x == 3:
        break
print("The end")
"""
"""
while True:
    x = input("Skriv något: ")
    if x == "quit":
        break
    else:
        print(x)
        print(len(x))
"""
"""
for x in "jensen":
    if x == "s":
        break
    print(x)
print("slut")
"""

"""
for x in "Jensen":
    if x == "e":
        continue
    print(x)
print("slut")
"""
"""
städer = ["Stockholm", "Sundsvall", "Göteborg"]
print(städer)
städer.append("Motala")
print(städer)
städer.insert(2, "Västerås")
print(städer)
städer.pop(0)
städer.remove("Motala")
print(städer)
städer[1]= "Eskilstuna"
print(städer)
städer.clear()
print(städer)
"""

fruits = ["Orange", "Apple", "Banana"]
if "Apple" in fruits:
    print("Apple isnt not exist")
else:
    print("Nuh uh")

