from conta_bancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    # Construtor
    def __init__(self, titular, senha):
        # Herança
        super().__init__(titular, senha)

    # Métodos
    def detalhar_conta(self):  # Polimorfismo
        return f"{self.titular} {self._ContaBancaria__saldo}"
    
    def sacar(self, valor):  # Polimorfismo
        if valor <= self._ContaBancaria__saldo and valor > 0:
            self._ContaBancaria__saldo -= valor
            return True
        return False
    
    def render_juros(self, porcentagem):
        rendimento = self._ContaBancaria__saldo * (porcentagem / 100)
        self._ContaBancaria__saldo += rendimento
        return self._ContaBancaria__saldo