from produtos_2 import Sedan, SUV

class SedanEletrico(Sedan): # Herda o produto carro Sedan
    # Métodos
    def descricao(self):
        return "Sedan Elétrico" # Retorna a descrição do Sedan Elétrico

class SUVEletrico(SUV): # Herda o produto carro SUV
    # Métodos
    def descricao(self):
        return "SUV Elétrico" # Retorna a descrição do SUV Elétrico