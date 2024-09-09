from fabrica_carro_1 import FabricaCarro # Importa a Fábrica Abstrata
from carro_eletrico_5 import SedanEletrico # Importa o Produto Abstrato
from carro_eletrico_5 import SUVEletrico # Importa o Produto Abstrato

class FabricaCarroEletrico(FabricaCarro):
    # Métodos criados obrigatoriamente por ter herdado da classe "FabricaCarro"
    def criar_sedan(self) -> object:
        return SedanEletrico() # Retorna um objeto do tipo Sedan Elétrico

    def criar_suv(self) -> object:
        return SUVEletrico() # Retorna um objeto do tipo SUV Elétrico