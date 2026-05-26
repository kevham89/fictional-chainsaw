while True:
    start = int(input("Skriv ett tal att börja med: "))
    slut = int(input("Skriv ett tal att sluta med: "))
    for x in range(start, slut +1, 1):
        print(x)
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue
