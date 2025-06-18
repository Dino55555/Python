def main():
    saldo = 0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500

    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
                continue

            valor = float(input("Informe o valor do saque: R$ "))

            if valor > LIMITE_POR_SAQUE:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_POR_SAQUE:.2f}.")
            elif valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > 0:
                saldo -= valor
                extrato.append(f"Saque:    R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in extrato:
                    print(movimento)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()