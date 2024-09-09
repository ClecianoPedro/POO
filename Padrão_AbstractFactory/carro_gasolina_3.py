from produtos_2 import Sedan, SUV # Importa os Produtos Abstratos

class SedanGasolina(Sedan): # Herda o produto carro Sedan
    # Métodos
    def descricao(self, descricao:str) -> str:
        self.descricao = descricao
        return descricao # Retorna a descrição do Sedan a gasolina



class SUVGasolina(SUV): # Herda o produto carro SUV
    # Métodos
    def descricao(self, descricao:str) -> str:
        self.descricao = descricao
        return descricao # Retorna a descrição do SUV a gasolina