klant = input("Naam van de klant: ")

aantal = int(input("Aantal producten: "))
prijs = float(input("Prijs per stuk: "))

subtotaal = aantal * prijs
btw = subtotaal * 0.21
totaal = subtotaal + btw

print("==============================")
print("Factuur voor:", klant)
print("Aantal producten:", aantal)
print("Prijs per stuk: €", prijs)
print("------------------------------")
print("Subtotaal: €", subtotaal)
print("BTW (21%): €", btw)
print("TOTAAL: €", totaal)
print("==============================")