while True:
    start = int(input("Skriv ett tal att börja med: "))
    for x in range(start, -1, -1):
        print(x)
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue
