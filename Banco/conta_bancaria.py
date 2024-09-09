from Exception.invalid_value_error import InvalidValue

class ContaBancaria:
    #Construtor
    def __init__(self, titular, senha):
        # Atributos
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0
    
    # Métodos
    def detalhar_conta(self):  # Polimorfismo
        pass
    
    def depositar(self, valor:int) -> bool:
        if valor > 0:
            self.__saldo += valor
            return True
        raise InvalidValue("Valor deve ser maior que zero")

    def sacar(self, valor:int):  # Polimorfismo
        pass

    def alterar_senha(self, nova_senha:str) -> bool:
        self.__senha = nova_senha
        return True

    def validar_senha(self, senha:str):
        if senha == self.__senha:
            return True
        return False