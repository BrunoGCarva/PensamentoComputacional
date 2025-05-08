from models.ContaCorrente import ContaCorrente
"""
Utilizar a Classe ContaBancaria para criar um menu no main.py, onde necessita ter as seguintes operações:
- 1: criar conta;
- 2: sacar
- 3: depositar
- 4 realizar transferência
- 5: excluir conta (solicitar conta para transferir o saldo restante, ou depositar o que falta para zerar a conta)
"""
Banco = []
a = 0
while a != 6:
    a = int(input("Informe a operação que deseja realizar\n1 para criar conta \n2 para sacar \n3 para depositar \n4 para realizar transferência \n5 para excluir conta\n"))
    if a == 1:
        titular = input("Informe o nome do titular da conta")
        saldo = float(input("Informe seu saldo atual"))
        limite = float(input("Informe o limite da conta"))
        Banco.append({titular,saldo,limite})
        nova_conta = ContaCorrente(titular,saldo,limite,[])
    if a == 2:
        
        saque= float(input("informe o valor do saque"))
        nova_conta.sacar(saque)
        
        


