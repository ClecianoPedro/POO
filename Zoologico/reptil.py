from animal import Animal

class Reptil(Animal):
    # Construtor
    def __init__(self, nome, idade, tipo_de_pele):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__tipo_de_pele = tipo_de_pele

    def movimentar(self):
        print("Rastejando")