from tipodejogo import TipoDeJogo
from jogador import Jogador

class Luta(TipoDeJogo):
    # Construtor
    def __init__(self, rounds = 3):
        # Herança
        super().__init__()
        # Atributos
        self.jogador1 = Jogador()
        self.jogador2 = Jogador()
        self.rounds = rounds

    # Métodos

    def determina_vencedor(self, resultado_rounds_jogador1, resultado_rounds_jogador2):
        if resultado_rounds_jogador1 > resultado_rounds_jogador2:
            return self.jogador1
        elif resultado_rounds_jogador2 > resultado_rounds_jogador1:
            return self.jogador2
        
    