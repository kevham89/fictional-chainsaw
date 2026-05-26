while True:
    resultat = 0
    n = int(input("Skriv ett tal: "))
    for x in range(1, n + 1):
        resultat += x
    print("Summan av talen från 1 till", n, "är:", resultat)
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue
