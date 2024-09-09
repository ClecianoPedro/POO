from produtos_2 import Sedan, SUV

class SedanGasolina(Sedan): # Herda o produto carro Sedan
    # Métodos
    def descricao(self):
        return "Sedan a Gasolina" # Retorna a descrição do Sedan a gasolina



class SUVGasolina(SUV): # Herda o produto carro SUV
    # Métodos
    def descricao(self):
        return "SUV a Gasolina" # Retorna a descrição do SUV a gasolina