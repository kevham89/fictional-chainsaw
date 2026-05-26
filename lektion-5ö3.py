poäng = int(input("Vad fick du för poäng? "))
if poäng >= 101:
    print("Maxpoäng är 100, vänligen försök igen.")
elif poäng >= 90:
    print("Ditt betyg är: A")
elif poäng >= 80:
    print("Ditt betyg är: B")
elif poäng >=70:
    print("Ditt betyg är: C")
elif poäng >=60:
    print("Ditt betyg är: D")
elif poäng >=50:
    print("Ditt betyg är: E")
else:
    print("Ej godkänt")