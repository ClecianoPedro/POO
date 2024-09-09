from ave import Ave
from mamifero import Mamifero
from reptil import Reptil

print("Mamifero")
mamifero = Mamifero("Onça", 5.0, True)
mamifero.fazer_som()
mamifero.movimentar()

print("Ave que não voa")
ave = Ave("Galinha", 0.2, False)
ave.fazer_som()
ave.movimentar()

print("Ave que voa")
ave2 = Ave("Pássaro", 1.5, True)
ave2.fazer_som()
ave2.movimentar()

print("Reptil")
reptil = Reptil("Lagarto", 1.8, "Escamosa")
reptil.fazer_som()
reptil.movimentar()