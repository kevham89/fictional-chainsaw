x = int(input("Skriv in ett tal "))
resultat = 0 
for n in range(1, x + 1):
    resultat = resultat + n
    print(n)
print("Summan av alla tal är =", resultat)


while True:
    n = int(input("Enter n:"))
    summan = 0
    counter = 1
    while counter <= n:
        summan = summan + counter
        counter = counter + 1
    print("the sum is:", summan)
