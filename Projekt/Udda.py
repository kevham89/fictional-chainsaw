def uddafärger():
    färg = ["Literöd", "Jättegrön", "Brandgul", "Blåmes"]
    for x in färg:
        print(x)
    while True:
        färgval = input("Välj en utav dessa färger, var noga med att stava rätt! ")
        if färgval == "Literöd":
            print("rödspådom")
            break
        elif färgval == "Jättegrön":
            print("grönspådom")
            break
        elif färgval == "Brandgul":
            print("gulspådom")
            break
        elif färgval == "Blåmes":
            print("Blåspådom")
            break
    else:
        print("Stavade du rätt? Försök igen. ")
        Continue
uddafärger()

