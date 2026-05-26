"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

"""

"""
frukt = ["apple", "banana", "cherry"]
typ = ["red", "big", "tasty"]
for x in typ:
    for y in frukt:
        print(x, y)
"""

"""
frukt = ["apple", "banana", "cherry"]
typ = ["red", "big", "tasty"]
count = 0
for x in frukt:
    print(typ[count], frukt[count])
    count += 1
"""
"""
frukt = ["apple", "banana", "cherry"]
typ = ["red", "big", "tasty"]
for x in range (len(typ)):
    print (typ[x], frukt[x])
"""
"""
frukt = ["apple", "banana", "cherry"]
typ = ["red", "big", "tasty"]
for x,y in zip(typ, frukt):
    print(x,y)
"""
"""
nummer = [1, 2, 3, 4]
if 1 in nummer:
    print("1 finns")
else:
    print("1 finns ej")
"""
"""
usernames = ["user1","user2","user3","user4","user5"]
for x in usernames:
    if x == "user3":
        continue
    else:
        print(x)

usernames = ["user1","user2","user3","user4","user5"]
for x in usernames:
    if x != "user3":
       print(x)
    else:
        continue
"""
"""
usernames = ["user1","user2","user3","user4","user5"]
print(usernames)
for x in usernames:
    if x == "user1":
        usernames.remove("user1")
        print(usernames)
        print("removed user1")
    else:
        continue
print("done")
"""
"""
def removeuser1():
    usernames = ["user1","user2","user3","user4","user5"]
    while "user1" in usernames:
        usernames.remove("user1")
        print("removed user1")
        for x in usernames:
            print(x)
removeuser1()
"""
"""
for x in range(4):
    if x !=3:
        print(x)
        continue
        print(x)
    else:
        print("test")
"""
"""
land = "Sverige"
print(land[:2])
print(land[3:6])
print(land[5:])
"""

"""
numbers = [1,2,3,4,5]
jensen = numbers
numbers.append(6)
print(numbers)
print(jensen)

numbers = [1,2,3,4,5]
jensen = numbers[:]
numbers.append(6)
print(numbers)
print(jensen)
"""
"""
num = [1,5,-29,86,7,-8]
print(min(num))
print(max(num))
print(sum(num))
copyArray = num[:]
print(num)
print(copyArray)
"""
"""
for x in dir(__builtins__):
    print(x)
"""
"""
import math
x = math.pi
print(x)
"""
import math
while True:
    radie = int(input("skriv in radien: "))
    area = math.pi * pow(radie, 2)
    print(round(area, 2))
    if radie == 0:
        break


