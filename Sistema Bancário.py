class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saque = 3
        self.limite_valor_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Você depositou R$ {valor:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saque:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_valor_saque:
            print("Valor do saque excede o limite de R$ 500.00.")
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Você sacou R$ {valor:.2f}")

    def exibir_extrato(self):
        print("\nExtrato:")
        for operacao in self.extrato:
            print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")

    def resetar_saques_diarios(self):
        self.saques_diarios = 0



def menu():
    conta = ContaBancaria()

    while True:
        print("\n--- Menu ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depositar: "))
            conta.depositar(valor)

        elif opcao == '2':
            valor = float(input("Digite o valor para sacar: "))
            conta.sacar(valor)

        elif opcao == '3':
            conta.exibir_extrato()

        elif opcao == '4':
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")



menu()
