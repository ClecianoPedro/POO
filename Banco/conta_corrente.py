from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    # Construtor
    def __init__(self, titular, senha, limite):
        # Herança
        super().__init__(titular, senha)
        # Atributos
        self.__limite_cheque_especial = limite

    # Métodos
    def detalhar_conta(self):  # Polimorfismo
        return f"{self.titular} {self._ContaBancaria__saldo} {self.__limite_cheque_especial}"
    
    def sacar(self, valor):  # Polimorfismo
        if valor <= self._ContaBancaria__saldo + self.__limite_cheque_especial and valor > 0:
            self._ContaBancaria__saldo -= valor
            return True
        return False
            
