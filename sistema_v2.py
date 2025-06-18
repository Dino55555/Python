def depositar(saldo, valor, extrato, /):
    """
    Realiza um depósito na conta.
    Parâmetros posicionais:
    - saldo: saldo atual da conta
    - valor: valor a ser depositado
    - extrato: lista de movimentações
    
    Retorna:
    - saldo atualizado
    - extrato atualizado
    """
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta.
    Parâmetros nomeados:
    - saldo: saldo atual da conta
    - valor: valor a ser sacado
    - extrato: lista de movimentações
    - limite: limite por saque
    - numero_saques: quantidade de saques já realizados
    - limite_saques: limite máximo de saques
    
    Retorna:
    - saldo atualizado
    - extrato atualizado
    - numero_saques atualizado
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato bancário.
    Parâmetros:
    - saldo: posicional
    - extrato: nomeado
    
    Não retorna valores, apenas imprime o extrato
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    """
    Cria um novo usuário (cliente) do banco.
    Parâmetros:
    - usuarios: lista de usuários existentes
    
    Retorna:
    - Lista de usuários atualizada
    """
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return usuarios
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    
    print("\nUsuário criado com sucesso!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    """
    Filtra um usuário pelo CPF.
    Parâmetros:
    - cpf: CPF a ser buscado
    - usuarios: lista de usuários
    
    Retorna:
    - O usuário encontrado ou None
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta bancária.
    Parâmetros:
    - agencia: número da agência
    - numero_conta: número da conta
    - usuarios: lista de usuários
    
    Retorna:
    - Dicionário com os dados da conta ou None se não encontrou usuário
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
        return None
    
    print("\nConta criada com sucesso!")
    return {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

def listar_contas(contas):
    """
    Lista todas as contas cadastradas.
    Parâmetros:
    - contas: lista de contas
    
    Não retorna valores, apenas imprime as contas
    """
    if not contas:
        print("\nNenhuma conta cadastrada!")
        return
    
    print("\n================ CONTAS ================")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)
    print("========================================")

def main():
    AGENCIA = "0001"
    LIMITE_POR_SAQUE = 500
    LIMITE_SAQUES = 3
    
    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
    
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Criar Conta
    [l] Listar Contas
    [q] Sair
    => """
    
    while True:
        opcao = input(menu).strip().lower()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            usuarios = criar_usuario(usuarios)
        
        elif opcao == "c":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            print("\nObrigado por usar nosso sistema bancário. Até mais!")
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()