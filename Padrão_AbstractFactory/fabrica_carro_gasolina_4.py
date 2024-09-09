from fabrica_carro_1 import FabricaCarro
from carro_gasolina_3 import SedanGasolina
from carro_gasolina_3 import SUVGasolina

class FabricaCarroGasolina(FabricaCarro):
    # Métodos criados obrigatoriamente por ter herdado da classe "FabricaCarro"
    def criar_sedan(self):
        return SedanGasolina() # Retorna um objeto do tipo Sedan a gasolina

    def criar_suv(self):
        return SUVGasolina() # Retorna um objeto do tipo SUV a gasolina