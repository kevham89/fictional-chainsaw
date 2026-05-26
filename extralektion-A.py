val = ("1. Addition", "2. Subtraktion", "3. Multiplikation", "4. Division", "5. Avsluta" )
for x in val:
    print(x)

while True:
    val = input("Ange ditt val (1-5): ").strip().lower()
    if val in ("addition", "1"):
        print("Du valde addition")
    elif val in ("subtraktion", "2"):
        print("Du valde subtraktion")  
    elif val in ("multiplikation", "3"):
        print("Du valde multiplikation")
    elif val in ("division", "4"):
        print("Du valde division")
    elif val in ("avsluta", "5"):
        print("Du valde att avsluta")
        break