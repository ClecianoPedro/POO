from fabrica_carro_gasolina_4 import FabricaCarroGasolina
from fabrica_carro_eletrico_6 import FabricaCarroEletrico

def main():
  # Instanciando a Fabrica de Carro a Gasolina
  fabrica_gasolina = FabricaCarroGasolina()
  # Criando Sedan a Gasolina
  sedan_gasolina = fabrica_gasolina.criar_sedan()
  # Criando SUV a Gasolina
  suv_gasolina = fabrica_gasolina.criar_suv()
  
  print(f"Sedan a Gasolina: {sedan_gasolina.descricao()}")
  print(f"SUV a Gasolina: {suv_gasolina.descricao()}\n")

  # Instanciando a Fabrica de Carro Eletrico
  fabrica_eletrico = FabricaCarroEletrico()
  # Criando Sedan Eletrico
  sedan_eletrico = fabrica_eletrico.criar_sedan()
  # Criando SUV Eletrico
  suv_eletrico = fabrica_eletrico.criar_suv()
  
  print(f"Sedan Eletrico: {sedan_eletrico.descricao()}")
  print(f"SUV Eletrico: {suv_eletrico.descricao()}")

if __name__ == "__main__":
  main()