from abc import ABC, abstractmethod # Importa os métodos de Abstração

class Sedan(ABC): # Classe Abstrata - Não pode ser instanciada
    # Métodos

    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def descricao(self)-> str:
        pass

class SUV(ABC): # Classe Abstrata - Não pode ser instanciada
    # Métodos
    @abstractmethod
    # Método Abstrato - Quem herdar essa classe é obrigado a criar esse método!
    def descricao(self) -> str:
        pass