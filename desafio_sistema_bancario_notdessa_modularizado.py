from datetime import datetime

LIMITE_SAQUES = 3
AGENCIA = "0001"

usuarios = []   
contas = []

nome = ""

endereco = "" #logradouro, cidade - estado
numero_conta = "" #sequencial começa com 1 #so pode ter 1 usuario
usuario = "" #pode ter mais de uma conta #filtra a lista de usuarios buscando o numero do cpf informado para cada usuario da lista
#se encontrar cria a conta
#se não encontrar msg de erro
saldo = 0
extrato = ""
valor = 0
limite = 500
numero_saques = 0
banco_name = "Banco NotDessa"
contato = "Git: notdessa"

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!".center(40))
    else:
        print("Valor inválido para depósito.".center(40))
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("Não será possível sacar.".center(40))
        print(" Limite de saque excedido.".center(40))
    elif valor > saldo:
        print("Saldo insuficiente.".center(40))
    elif numero_saques >= limite_saques:
        print("Limite de saques atingido.".center(40))
    elif valor <= 0:
        print("Valor inválido.".center(40))
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!".center(40))

    return saldo, extrato, numero_saques

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario_existente = any(usuario["cpf"] == cpf for usuario in usuarios)
    if usuario_existente:
        print("Usuário já existente com esse CPF.".center(40))
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    try:
        datetime.strptime(data_nascimento, "%d-%m-%Y")
    except ValueError:
        print("Data de nascimento inválida.".center(40))
        return
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!".center(40))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print("Conta criada com sucesso!".center(40))
        print(f"Agência: {agencia} | Conta: {numero_conta}".center(40))
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    else:
        print("Usuário não encontrado.".center(40))
        return None

menu = f"""
==============================
 Bem-vindo ao {banco_name}!
==============================
Escolha uma operação:

[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite de Saque Diário
[n] Novo Usuário
[cc] Criar Conta Corrente
[lc] Listar Contas
[c] Contato
[q] Sair

==============================

=> """



while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido. Use apenas números.")
        continue
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido. Use apenas números.")
            continue
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        print("\n========== EXTRATO ==========".center(40))
        print("Não foram realizadas movimentações.".center(40) if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}".center(40))
        print("=============================".center(40))

    elif opcao == "l":
        print(f"\nLimite diário de saque: R$ {limite:.2f}".center(40))

    elif opcao == "c":
        print(" Contato ".center(40, "="))
        print("\nContato: suporte@notdessabank.com")
        print("Telefone: 0800-123-456")
        print(f"{contato}")
        print("\n")
        print("Caso tenha alguma dúvida,".center(40))
        print("entre em contato conosco.".center(40))
        print("\n")
        print("Volte Sempre!".center(40))
        print("=".center(40, "="))
    
    elif opcao == "n":
        criar_usuario(usuarios)

    elif opcao == "cc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "lc":
        for conta in contas:
            linha = f"""\
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            """
            print("="*40)
            print(linha.center(40))


    elif opcao == "q":
        print(" Sair ".center(40, "="))
        print(f"Obrigado por usar {banco_name}!".center(40))
        print("Tenha um bom dia!".center(40))
        print("=".center(40, "="))
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.".center(40))
        continue