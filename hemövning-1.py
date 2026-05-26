ämnen = ["matte", "datorteknik", "nätverksteknik"]
print(len(ämnen))
ämnen.append("programmering")
print(ämnen)
ämnen.insert(1, "natverksteknologier")
print(ämnen)
ämnen.pop(2)
print(ämnen)
ämnen.remove("matte")
print(ämnen)
for x in ämnen:
    print(x)
ämnen.clear()
print(ämnen)