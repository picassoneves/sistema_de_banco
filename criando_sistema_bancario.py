saldo = 0.0
limite = 500.0
extrato = ""
numero_de_saques = 0
LIMITES_DE_SAQUE = 3
total_saque = 0.0

while True:
    print('''\nBanco do Manuel
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair do sistema
    ''')
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número entre 1 e 4.")
        continue

    if opcao_escolhida == 1:
        try:
            deposito = float(input("Quanto você quer depositar? "))
        except ValueError:
            print("Valor inválido! Tente novamente.")
            continue

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação inválida! O valor do depósito deve ser positivo.")

    elif opcao_escolhida == 2:
        try:
            saque = float(input("Quanto você deseja sacar? "))
        except ValueError:
            print("Valor inválido! Tente novamente.")
            continue

        if saque <= 0:
            print("Você não pode sacar valores menores ou iguais a zero!")
            continue

        if saque > saldo:
            print("Operação falhou! Saldo insuficiente.")
            continue

        if saque > limite:
            print("Operação falhou! O valor do saque excede o limite de R$500 por saque.")
            continue

        if numero_de_saques >= LIMITES_DE_SAQUE:
            print("Limite de saques diários atingido.")
            continue

        if total_saque + saque > 500:
            print("Operação falhou! O total de saques não pode ultrapassar R$500.")
            continue

        saldo -= saque
        total_saque += saque
        numero_de_saques += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print("Saque realizado com sucesso!")

    elif opcao_escolhida == 3:
        print("\n========== Extrato ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao_escolhida == 4:
        print("Encerrando o sistema...")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
