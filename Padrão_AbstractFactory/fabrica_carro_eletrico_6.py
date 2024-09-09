from fabrica_carro_1 import FabricaCarro
from carro_eletrico_5 import SedanEletrico
from carro_eletrico_5 import SUVEletrico

class FabricaCarroEletrico(FabricaCarro):
    # Métodos criados obrigatoriamente por ter herdado da classe "FabricaCarro"
    def criar_sedan(self):
        return SedanEletrico() # Retorna um objeto do tipo Sedan Elétrico

    def criar_suv(self):
        return SUVEletrico() # Retorna um objeto do tipo SUV Elétrico