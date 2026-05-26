while True:
    start = int(input("Skriv ett tal att börja med: "))
    slut = int(input("Skriv ett tal att sluta med: "))
    steg = int(input("Skriv ett tal för antal steg mellan numren: "))
    for x in range(start, slut +1, steg):
        print(x)
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue
