from models.ContaCorrente import ContaCorrente

banco = []

def encontrar_conta(nome):
    for conta in banco:
        if conta.titular == nome:
            return conta
    return None

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Criar conta")
        print("2 - Exibir saldo")
        print("3 - Sacar")
        print("4 - Depositar")
        print("5 - Transferência")
        print("6 - Exibir histórico de transações")
        print("7 - Excluir conta")
        print("8 - Transferência PIX")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titular = input("Nome do titular: ")
            saldo = float(input("Saldo inicial: "))
            limite = float(input("Limite da conta: "))
            chavepix = input("Chave PIX: ")
            nova_conta = ContaCorrente(titular, saldo, limite, [],chavepix)
            banco.append(nova_conta)
            print("Conta criada com sucesso!")

        elif escolha == "2":
            titular = input("Nome do titular: ")
            conta = encontrar_conta(titular)
            if conta:
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
            else:
                print("Conta não encontrada.")

        elif escolha == "3":
            titular = input("Nome do titular: ")
            conta = encontrar_conta(titular)
            if conta:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif escolha == "4":
            titular = input("Nome do titular: ")
            conta = encontrar_conta(titular)
            if conta:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif escolha == "5":
            remetente_nome = input("Nome do remetente: ")
            destinatario_nome = input("Nome do destinatário: ")
            valor = float(input("Valor a transferir: "))
            remetente = encontrar_conta(remetente_nome)
            destinatario = encontrar_conta(destinatario_nome)
            if remetente and destinatario:
                remetente.transferir(destinatario, valor)
            else:
                print("Conta(s) não encontrada(s).")

        elif escolha == "6":
            titular = input("Nome do titular: ")
            conta = encontrar_conta(titular)
            if conta:
                conta.exibir_historico()
            else:
                print("Conta não encontrada.")

        elif escolha == "7":
            titular = input("Nome da conta a excluir: ")
            conta = encontrar_conta(titular)
            if conta:
                if conta.saldo > 0:
                    print(f"A conta possui R$ {conta.saldo:.2f} em saldo.")
                    destino_nome = input("Transferir saldo para qual conta? ")
                    destino = encontrar_conta(destino_nome)
                    if destino and destino != conta:
                        conta.transferir(destino, conta.saldo)
                        banco.remove(conta)
                        print("Conta excluída com sucesso após transferência.")
                    else:
                        print("Conta de destino inválida.")
                elif conta.saldo < 0:
                    print("Conta com saldo negativo. Deposite para zerar antes de excluir.")
                else:
                    banco.remove(conta)
                    print("Conta excluída com sucesso.")
            else:
                print("Conta não encontrada.")
        elif escolha == "8":
            remetente_nome = input("Nome do remetente: ")
            destinatariopix = input("Insira o pix do destinatário: ")
            valor = float(input("Valor a transferir: "))
            remetente = encontrar_conta(remetente_nome)
            destinatario = next((conta for conta in banco if conta.chavepix == destinatariopix), None)
            if remetente and destinatario:
                remetente.pix(destinatario, valor)
            else:
                print("Conta(s) não encontrada(s).")
        elif escolha == "11":
            break
        else:
            print("Opção inválida.")

menu()
