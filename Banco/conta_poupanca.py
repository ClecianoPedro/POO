from conta_bancaria import ContaBancaria
from Exception.invalid_value_error import InvalidValue

class ContaPoupanca(ContaBancaria):
    # Construtor
    def __init__(self, titular, senha):
        # Herança
        super().__init__(titular, senha)

    # Métodos
    def detalhar_conta(self):  # Polimorfismo
        return f"{self.titular} {self._ContaBancaria__saldo}"
    
    def sacar(self, valor:int) -> bool: # Polimorfismo
        if isinstance(valor, int):
            if valor <= 0:
                raise InvalidValue("Valor deve ser maior que zero")
        
            if valor <= self._ContaBancaria__saldo:
                self._ContaBancaria__saldo -= valor
                return True
        return False
    
    def render_juros(self, porcentagem):
        rendimento = self._ContaBancaria__saldo * (porcentagem / 100)
        self._ContaBancaria__saldo += rendimento
        return self._ContaBancaria__saldo