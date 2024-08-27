from animal import Animal

class Reptil(Animal):
    # Construtor
    def __init__(self, nome:str, idade:float, tipo_de_pele:str):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__tipo_de_pele = tipo_de_pele

    def fazer_som(self):
        print("O réptil está grunhindo.")
    
    def movimentar(self):
        print("O réptil está rastejando")