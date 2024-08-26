from animal import Animal

class Ave(Animal):
    # Contrutor
    def __init__(self, nome, idade, pode_voar):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__pode_voar = pode_voar

    # Métodos

    def movimentar(self):
        if self.__pode_voar == True:
            print("Voando")
        else:
            print("Andando")