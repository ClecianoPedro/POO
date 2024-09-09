from abc import ABC, abstractmethod # Importa os métodos de Abstração

class FabricaCarro(ABC): # Classe Abstrata - Não pode ser instanciada
    # Métodos
    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def criar_sedan(self) -> object:
        pass
    
    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def criar_suv(self) -> object:
        pass