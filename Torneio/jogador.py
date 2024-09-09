
class Jogador:
    # Construtor
    def __init__(self, nome, idade, sexo):
        # Atributos
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.pontuacao = 0
    
    # Métodos

    def atualiza_pontuacao(self, pontos):
        self.pontuacao += pontos