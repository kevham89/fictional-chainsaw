while True:
    ord = input("Skriv ett ord eller en hel mening: ")
    print("Antalet tecken i det du skrev är:", len(ord))
    stop = input("Vill du fortsätta? (ja/nej): ")
    if stop != "ja":
        break
    else:
        continue