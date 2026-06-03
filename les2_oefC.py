getal1 = int(input("Geef het eerste getal: "))
getal2 = int(input("Geef het tweede getal: "))

som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2

print("Som:", som)
print("Verschil:", verschil)
print("Product:", product)
print("Deling:", deling)

if getal1 % 2 == 0:
    print("Het eerste getal is even.")
else:
    print("Het eerste getal is oneven.")

print("Kwadraat van het eerste getal:", getal1 ** 2)