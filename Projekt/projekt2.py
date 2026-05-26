count2 = 0 # fördefinerar ett värde på våran räknare.
val = input("skriv in en fråga: ")  # Ber användaren att skriva in fråga som en sträng.
for len in val: # räknar antalet bokstäver i användarens fråga och använder det som en range för våran loop.
	count2 += 1 # adderar 1 till våran räknare varje gång vi loopar koden.
	if count2 == 3: # kollar om våran räknare är lika med 3
		count2 = 1  # återställer räknaren till 1 så att vi endast kollar om talet blir 1 eller 2.
if count2 == 1: # om våran räknare stannar på 1 så kommer nedan kod att köras.
	def uddafärger(): # Vi skapar en funktion som innehåller nedan kod (redundant men visar att det går att göra)
		färg = ["Literöd", "Jättegrön", "Brandgul", "Blåmes"] # Vi börjar med att lägga in 4 stycken färger i en lista. 
		for x in färg: # Vi skapar en for loop som körs lika många gånger som antalet element i våran lista.
			print(x) # Vi skriver ut färgerna till användaren i terminal, en färg per rad. 
		while True: # Vi startar en While loop som alltid är aktiv
			färgval = input("Välj en utav dessa färger, var noga med att stava rätt! ") # Vi ber användaren att välja en utav de 4 färgerna. 
			if färgval.capitalize() == "Literöd": # Om användaren väljer "Literöd" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Ja, utan tvekan. ") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Jättegrön": # Om användaren väljer "Jättegrön" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Tecken pekar på ja. ") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Brandgul": # Om användaren väljer "Brandgul" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Fråga igen senare.") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Blåmes": # Om användaren väljer "Blåmes" så skriver vi ut en "spådom" till användaren och stoppar koden (Vi vet att det är en fågel)
				print("Mina källor säger nej.") # Skriver ut "spådommen"
				break #Stoppar koden
			else:
				print("Stavade du rätt? Försök igen. ") # Om användaren stavar fel och/eller väljer en färg som inte finns på listan så ber vi dem att försöka igen och startar om koden från while loopen.
				continue
	uddafärger() # Här ropar vi på våran funktion som vi skapade ovan och ber programmet att köra koden. Det är framförallt användbart om vi behöver köra koden flera gånger i programmet men här gör vi det bara 1 gång.
else: # om våran räknare stannar på 2 så kommer nedan kod att köras.
	def jämnafärger():  # Vi skapar en funktion som innehåller nedan kod (redundant men visar att det går att göra)
		färg = ["Rosa", "Lila", "Turkos", "Beige"] # Vi ber användaren att välja en utav de 4 färgerna.
		for x in färg: # Vi skapar en for loop som körs lika många gånger som antalet element i våran lista.
			print(x)  # Vi skriver ut färgerna till användaren i terminal, en färg per rad. 
		while True: # Vi startar en While loop som alltid är aktiv
			färgval = input("Välj en av dessa färger, obs var noga med att stava rätt! ") # Vi ber användaren att välja en utav de 4 färgerna. 
			if färgval == "Rosa": # Om användaren väljer "Rosa" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Innan veckan är slut") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Lila": # Om användaren väljer "Lila" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Mest troligt imorgon ") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Turkos": # Om användaren väljer "Turkos" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Nej, det är inte möjligt ") # Skriver ut "spådommen"
				break #Stoppar koden
			elif färgval == "Beige": # Om användaren väljer "Beige" så skriver vi ut en "spådom" till användaren och stoppar koden
				print("Efter regn kommer sol, blicka frammåt ") # Skriver ut "spådommen"
				break #Stoppar koden
			else:
				print("Stavade du rätt? Försök igen ") # Om användaren stavar fel och/eller väljer en färg som inte finns på listan så ber vi dem att försöka igen och startar om koden från while loopen.
				continue
	jämnafärger()  # Här ropar vi på våran funktion som vi skapade ovan och ber programmet att köra koden. Det är framförallt användbart om vi behöver köra koden flera gånger i programmet men här gör vi det bara 1 gång.