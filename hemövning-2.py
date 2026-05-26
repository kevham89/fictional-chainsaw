"""
while True:
    tal = int(input("Gissa ett tal mellan 1-100: "))
    if tal != 70:
        print("Fel, gissa igen.")
    else:
        print("Grattis, du gissade rätt!")
        break
"""

while True:
    tal = input("Gissa ett tal mellan 1-100: ")
    if tal != "70":
        print("Fel, gissa igen.")
    else:
        print("Grattis, du gissade rätt!")
        break