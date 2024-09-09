
class Partida:
    # Construtor
    def __init__(self, jogador1, jogador2):
        # Atributos
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    # Métodos

    def cria_partida(self) -> object:
        return Partida(self.jogador1, self.jogador2)
    
    def registra_resultado(self, jogador_vencedor, jogador_perdedor):
        resultado = jogador_vencedor, jogador_perdedor
        return resultado