
class Torneio:
    # Construtor
    def __init__(self, nome:str):
        # Atributos
        self.nome = nome
        self.__jogadores = []
        self.__partidas = []
        self.__ranking = []

    # Métodos

    def adiciona_jogador(self, jogador:object):
        self.__jogadores.append(jogador)

    def gera_ranking(self):
        self.ranking = sorted(self.ranking, reverse=True)

    def exibe_ranking(self):
        for i in self.ranking:
            print(f"{i}º Jogador:  Pontuação: ")
    
    def calcula_pontuacao(self):
        pass
