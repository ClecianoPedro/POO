from animal import Animal

class Ave(Animal):
    # Contrutor
    def __init__(self, nome:str, idade:float, pode_voar:bool):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__pode_voar = pode_voar

    # Métodos

    def fazer_som(self):
        print("A ave está cantando.")

    def movimentar(self):
        if self.__pode_voar == True:
            print("A ave está voando")
        else:
            print("A ave está andando")