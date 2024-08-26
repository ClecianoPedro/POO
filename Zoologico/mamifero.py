from animal import Animal

class Mamifero(Animal):
    # Construtor
    def __init__(self, nome, idade, tem_pelo):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__tem_pelo = tem_pelo

        # Métodos

        def fazer_som(self):
            print("O mamífero está rugindo.")
        
