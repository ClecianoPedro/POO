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
    
    def depositar(self, valor):
        self.__saldo += valor
        return True

    def sacar(self, valor):  # Polimorfismo
        pass

    def alterar_senha(self, nova_senha):
        self.__senha = nova_senha
        return True

    def validar_senha(self, senha):
        if senha == self.__senha:
            return True
        return False