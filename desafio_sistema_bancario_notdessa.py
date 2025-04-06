saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
banco_name = "Banco NotDessa"
contato = "git_username: notdessa"

menu = f"""
==============================
 Bem-vindo ao {banco_name}!
==============================
Escolha uma operação:

[d] Depositar
[s] Sacar
[e] Extrato
[l] Limite de Saque Diário
[c] Contato
[q] Sair

==============================

=> """


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ".center(40)))
        print(" Depósito".center(40, "="))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!".center(40))
        else:
            print("Valor insuficiente para depósito.".center(40))
        print("=".center(40, "="))

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: ").center(40)) 
        print(" Saque ".center(40, "="))

        if valor > limite:
            print("Não será possível sacar.".center(40))
            print(" Limite de saque excedido.".center(40))
            
        elif valor <= saldo and numero_saques < LIMITE_SAQUES and valor > 0:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!".center(40))
            print(f"Limite de saques: {LIMITE_SAQUES - numero_saques} saques restantes.".center(40))

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido.".center(40))

        else:
            print("Valor inválido.".center(40))
        print("=".center(40, "="))

    
    elif opcao == "e":
        print(" Extrato ".center(40, "="))
        if not extrato:
            print(f"Saldo: R$ {saldo:.2f}".center(40))
            print(f"Limite de saques: {LIMITE_SAQUES - numero_saques} saques restantes.".center(40))
            print("Não foram realizadas movimentações.".center(40))
        else:
            print(extrato.center(40))
            print(f"Saldo: R$ {saldo:.2f}".center(40))
            print(f"Limite de saques: {LIMITE_SAQUES - numero_saques} saques restantes.".center(40))
        print("=".center(40, "="))

    elif opcao == "l":
        print(" Limite de Saque Diário ".center(40, "="))
        print(f"Limite de saques: {LIMITE_SAQUES - numero_saques} saques restantes.".center(40))
        print(f"Limite de saque diário: R$ {limite:.2f}".center(40))
        print("=".center(40, "="))

    elif opcao == "c":
        print(" Contato ".center(40, "="))
        print(f"{contato}".center(40))
        print("Caso tenha alguma dúvida,".center(40))
        print("entre em contato conosco.".center(40))
        print("Estamos aqui para ajudar!".center(40))
        print("=".center(40, "="))
    
    elif opcao == "q":
        print(" Sair ".center(40, "="))
        print(f"Obrigado por usar {banco_name}!".center(40))
        print("Tenha um bom dia!".center(40))
        print("=".center(40, "="))
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.".center(40))
        continue