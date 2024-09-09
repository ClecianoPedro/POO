from tipodejogo import TipoDeJogo
from jogador import Jogador

class Corrida(TipoDeJogo):
    # Construtor
    def __init__(self):
        # Herança
        super().__init__()
        # Atributos
        self.jogador1 = Jogador()
        self.jogador2 = Jogador()
        self.tempo = 0.0

    # Métodos

    def determina_vencedor(self, tempo_jogador1:float, tempo_jogador2:float):
        if tempo_jogador1 > tempo_jogador2:
            return self.jogador1
        elif tempo_jogador2 > tempo_jogador1:
            return self.jogador2