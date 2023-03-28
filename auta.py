class auto:
  def __init__(self, znacka, model, barva, karoserie ):
    self.znacka = znacka
    self.model = model
    self.barva = barva
    self.karoserie = karoserie
    

moje_a1 = auto("BMW", "M5", "modrá", "sedan")
tvoje_a2 = auto ("Audi", "A3", "černá", "SUV")

print("Moje auto je:")
print(moje_a1.znacka)
print(moje_a1.model)
print(moje_a1.barva)
print(moje_a1.karoserie)
print("Tvoje auto je:")
print(tvoje_a2.znacka)
print(tvoje_a2.model)
print(tvoje_a2.barva)
print(tvoje_a2.karoserie)