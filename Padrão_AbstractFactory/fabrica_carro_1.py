from abc import ABC, abstractmethod

class FabricaCarro(ABC): # Classe Abstrata - Não pode ser instanciada
    # Métodos
    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def criar_sedan(self):
        pass
    
    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def criar_suv(self):
        pass