from conta_bancaria import ContaBancaria
from Exception.invalid_value_error import InvalidValue

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
        if isinstance(valor, int):
            if valor <= 0:
                raise InvalidValue("Valor deve ser maior que zero")
        
            if valor <= self._ContaBancaria__saldo + self.__limite_cheque_especial:
                self._ContaBancaria__saldo -= valor
                return True
        return False
            
