from fabrica_carro_1 import FabricaCarro # Importa a Fábrica Abstrata
from carro_gasolina_3 import SedanGasolina # Importa o Produto Abstrato
from carro_gasolina_3 import SUVGasolina # Importa o Produto Abstrato

class FabricaCarroGasolina(FabricaCarro):
    # Métodos criados obrigatoriamente por ter herdado da classe "FabricaCarro"
    def criar_sedan(self) -> object:
        return SedanGasolina() # Retorna um objeto do tipo Sedan a gasolina

    def criar_suv(self) -> object:
        return SUVGasolina() # Retorna um objeto do tipo SUV a gasolina