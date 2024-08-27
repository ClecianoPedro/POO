from animal import Animal

class Mamifero(Animal):
    # Construtor
    def __init__(self, nome:str, idade:float, tem_pelo:bool):
        # Herança
        super().__init__(nome, idade)
        # Atributos
        self.__tem_pelo = tem_pelo

        # Métodos

    def fazer_som(self):
        print("O mamífero está rugindo.")
        
    def movimentar(self):
        print("O mamífero está se movendo.")