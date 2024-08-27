from abc import abstractmethod, ABC

class Animal(ABC):
    # Construtor
    def __init__(self, nome, idade):
        # Atributos
        self.__nome = nome
        self.__idade = idade

    # Métodos
    @abstractmethod
    def fazer_som(self): # Polimorfismo
        pass

    @abstractmethod
    def movimentar(self): # Polimorfismo
        pass