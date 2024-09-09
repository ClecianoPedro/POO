from fabrica_carro_gasolina_4 import FabricaCarroGasolina
from fabrica_carro_eletrico_6 import FabricaCarroEletrico

def main():
  # Instanciando a Fabrica de Carro a Gasolina
  fabrica_gasolina = FabricaCarroGasolina()
  # Criando Sedan a Gasolina
  sedan_gasolina = fabrica_gasolina.criar_sedan()
  # Criando SUV a Gasolina
  suv_gasolina = fabrica_gasolina.criar_suv()
  
  print(f"Sedan a Gasolina: {sedan_gasolina.descricao("Sedan a Gasolina")}")
  print(f"SUV a Gasolina: {suv_gasolina.descricao("SUV a Gasolina")}\n")

  # Instanciando a Fabrica de Carro Elétrico
  fabrica_eletrico = FabricaCarroEletrico()
  # Criando Sedan Elétrico
  sedan_eletrico = fabrica_eletrico.criar_sedan()
  # Criando SUV Elétrico
  suv_eletrico = fabrica_eletrico.criar_suv()
  
  print(f"Sedan Elétrico: {sedan_eletrico.descricao("Sedan Elétrico")}")
  print(f"SUV Elétrico: {suv_eletrico.descricao("SUV Elétrico")}")

if __name__ == "__main__":
  main()