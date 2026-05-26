x = 2
while x <= 200:
    print(x)
    x = x + 2

"""
In this specific code, the x >= 20 condition is actually redundant and serves no functional purpose.
Since x starts at 20 and only ever increases (by 2 each iteration), it can never drop below 20, so that condition will always be True and never actually stops the loop.
"""
x = 20
while x >= 20 and x <= 40:
    print(x)
    x = x + 2

x = 2
while True:
    print(x)
    x = x + 2
    if x == 100:
        break