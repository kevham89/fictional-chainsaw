def uddafärger(): # Vi skapar en funktion som innehåller nedan kod (redundant men visar att det går att göra)
	färg = ["Literöd", "Jättegrön", "Brandgul", "Blåmes"] # Vi börjar med att lägga in 4 stycken färger i en lista. 
	for x in färg: # Vi skapar en for loop som körs lika många gånger som antalet element i våran lista.
		print(x) # Vi skriver ut färgerna till användaren i terminal, en färg per rad. 
	while True: # Vi startar en While loop som alltid är aktiv
		färgval = input("Välj en utav dessa färger, var noga med att stava rätt! ") # Vi ber användaren att välja en utav de 4 färgerna. 
		if färgval.lower() == "literöd": # Om användaren väljer "Literöd" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Ja, utan tvekan. ") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "jättegrön": # Om användaren väljer "Jättegrön" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Tecken pekar på ja. ") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "brandgul": # Om användaren väljer "Brandgul" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Fråga igen senare.") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "blåmes": # Om användaren väljer "Blåmes" så skriver vi ut en "spådom" till användaren och stoppar koden (Vi vet att det är en fågel)
			print("Mina källor säger nej.") # Skriver ut "spådommen"
			break #Stoppar koden
		else:
			print("Stavade du rätt? Försök igen. ") # Om användaren stavar fel och/eller väljer en färg som inte finns på listan så ber vi dem att försöka igen och startar om koden från while loopen.
			continue

def jämnafärger():  # Vi skapar en funktion som innehåller nedan kod (redundant men visar att det går att göra)
	färg = ["Rosa", "Lila", "Turkos", "Beige"] # Vi ber användaren att välja en utav de 4 färgerna.
	for x in färg: # Vi skapar en for loop som körs lika många gånger som antalet element i våran lista.
		print(x)  # Vi skriver ut färgerna till användaren i terminal, en färg per rad. 
	while True: # Vi startar en While loop som alltid är aktiv
		färgval = input("Välj en av dessa färger, obs var noga med att stava rätt! ") # Vi ber användaren att välja en utav de 4 färgerna. 
		if färgval.lower() == "rosa": # Om användaren väljer "Rosa" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Innan veckan är slut") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "lila": # Om användaren väljer "Lila" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Mest troligt imorgon ") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "turkos": # Om användaren väljer "Turkos" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Nej, det är inte möjligt ") # Skriver ut "spådommen"
			break #Stoppar koden
		elif färgval.lower() == "beige": # Om användaren väljer "Beige" så skriver vi ut en "spådom" till användaren och stoppar koden
			print("Efter regn kommer sol, blicka frammåt ") # Skriver ut "spådommen"
			break #Stoppar koden
		else:
			print("Stavade du rätt? Försök igen ") # Om användaren stavar fel och/eller väljer en färg som inte finns på listan så ber vi dem att försöka igen och startar om koden från while loopen.
			continue


while True:
	count2 = 0
	val = input("Ställ en ja eller nej fråga: ")
	for len in val:
		count2 += 1
		if count2 == 3:
			count2 = 1
	while True:
		if count2 == 1:
			uddafärger()
			break
		elif count2 == 2:
			jämnafärger()
			break
		else:
			print("Något gick fel.")
			continue
	val2 = input("Vill du ställa en ny fråga? (ja/nej) ")
	if val2.lower() == "ja":
		continue
	elif val2.lower() == "nej":
		break
	else:
		print("Osäker? testa att fråga vår spådomsloppa igen!")
		continue