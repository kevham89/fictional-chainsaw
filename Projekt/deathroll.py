import random

rollrange = 1000

while True:
    # My roll
    input("Press Enter to roll for me...")
    me = random.randint(1, rollrange)
    print("I rolled:", me)
    if me == 1:
        print("I lost!")
        break
    rollrange = me

    # Your roll
    input("Press Enter to roll for you...")
    you = random.randint(1, rollrange)
    print("You rolled:", you)
    if you == 1:
        print("You lost!")
        break
    rollrange = you