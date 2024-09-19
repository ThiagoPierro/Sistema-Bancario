class ContaBancaria:
    def __init__(self, agencia, numero_conta, cpf, nome):
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saque = 3
        self.limite_valor_saque = 500.0
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cpf = cpf
        self.nome = nome

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

    def exibir_dados(self):
        print(f"Agência: {self.agencia}, Conta: {self.numero_conta}, CPF: {self.cpf}, Nome: {self.nome}")



contas_criadas = []


def criar_conta():
    agencia = input("Digite o número da agência: ")
    numero_conta = input("Digite o número da conta: ")
    cpf = input("Digite seu CPF (11 dígitos): ")
    nome = input("Digite seu nome: ")

    if len(cpf) == 11 and cpf.isdigit():
        conta = ContaBancaria(agencia, numero_conta, cpf, nome)
        contas_criadas.append(conta)  # Adiciona a conta na lista
        print("Conta criada com sucesso!")
        return conta
    else:
        print("CPF inválido. Criação de conta encerrada.")
        return None


def listar_contas():
    if contas_criadas:
        print("\n--- Contas Criadas ---")
        for conta in contas_criadas:
            conta.exibir_dados()
    else:
        print("Nenhuma conta criada ainda.")


def menu(conta):
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



def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar Nova Conta")
        print("2. Listar Contas Criadas")
        print("3. Acessar Conta (Fazer Operações)")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_conta()

        elif opcao == '2':
            listar_contas()

        elif opcao == '3':
            if contas_criadas:
                cpf = input("Digite o CPF da conta que deseja acessar: ")
                conta_encontrada = None
                for conta in contas_criadas:
                    if conta.cpf == cpf:
                        conta_encontrada = conta
                        break

                if conta_encontrada:
                    menu(conta_encontrada)
                else:
                    print("Conta não encontrada.")
            else:
                print("Nenhuma conta criada para acessar.")

        elif opcao == '4':
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")



menu_principal()

