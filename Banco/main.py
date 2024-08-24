from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def menu_conta():
    print("1 - Detalhes da Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Alterar senha")
    print("5 - Validar senha")
    print("0 - Sair")
    opcao = int(input("Digite a opcao: "))
    return opcao

def main():
    conta_poupanca = ContaPoupanca("Cleciano", "123456")
    conta_corrente = ContaCorrente ("Pedro", "123456", 1000)
    print("Testando Classes...")
    print("Conta Poupança")
    print(conta_poupanca.detalhar_conta())
    conta_poupanca.depositar(500)
    print(conta_poupanca.detalhar_conta())
    conta_poupanca.sacar(200)
    print(conta_poupanca.detalhar_conta())
    print(conta_poupanca.render_juros(10))
    print("Conta Corrente")
    print(conta_corrente.detalhar_conta())
    conta_corrente.depositar(1000)
    print(conta_corrente.detalhar_conta())
    conta_corrente.sacar(2000)
    print(conta_corrente.detalhar_conta())
    conta_corrente.depositar(500)
    print(conta_corrente.detalhar_conta())
    print("Fim do Teste...")

    opcao = 1
    while opcao != 0:
        opcao = menu_conta()
        if opcao == 1:
            print(conta_poupanca.detalhar_conta())

        elif opcao == 2:
            valor = int(input("Digite o valor a ser depositado: "))
            conta_poupanca.depositar(valor)
            print("Depósito realizado com sucesso!")

        elif opcao == 3:
            valor = int(input("Digite o valor a ser sacado: "))
            retorno = conta_poupanca.sacar(valor)
            if retorno:
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")

        elif opcao == 4:
            nova_senha = input("Digite a nova senha: ")
            conta_poupanca.alterar_senha(nova_senha)
            print("Senha alterada com sucesso!")

        elif opcao == 5:
            senha = input("Digite sua senha: ")
            if conta_poupanca.validar_senha(senha):
                print("Senha correta!")
            else:
                print("Senha incorreta!")

        elif opcao == 0:
            print("Encerrando...")
            opcao = 0

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()