while True:
    ord = input("Skriv ett ord: ")
    tal = int(input("Skriv ett tal: "))
    for x in range (1, tal + 1):
        print(x, ord)
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue