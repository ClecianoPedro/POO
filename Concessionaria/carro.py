class Carro:
    # Caracteristicas - Atributo - Variavel
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    # Comportamentos - Metodos - Funcoes
    def exibir_infos(self):
        print(f"{self.marca} {self.modelo} {self.ano}")

    def acelerar(self):
        self.velocidade += 15

    def frear(self):
        self.velocidade -= 15