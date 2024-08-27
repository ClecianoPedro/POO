from ave import Ave
from mamifero import Mamifero
from reptil import Reptil

print("Mamifero\n")
mamifero = Mamifero("Onça", 10, True)
mamifero.fazer_som()
mamifero.movimentar()

print("Ave\n")
ave = Ave("Galinha", 0.2, False)
ave.fazer_som()
ave.movimentar()
print("Ave 2\n")
ave2 = Ave("Pássaro", 2, True)
ave2.fazer_som()
ave2.movimentar()

print("Reptil\n")
reptil = Reptil("Lagarto", 2, "Escamosa")
reptil.fazer_som()
reptil.movimentar()