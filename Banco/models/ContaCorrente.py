import time
class ContaCorrente:
    """
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular(str), saldo(float), limite(float), historico(lista de dicionários)
    
    OBS: Operações no histórico: 0 - sacar, 1- depositar, 2 - transferir
    """
    
    def __init__(self,titular, saldo, limite,historico):
        """
        Construtor da classe CntaBancária
        """
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    def depositar(self, valor):
        """
        método que realiza do depósito na conta bancária.
        Entrada: valor(float)
        return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        """
        if valor > 0:
            self.saldo += valor
            self.historico.append({
                "operacao": 1,
                "remetente": self.titular,
                "destinatario": "",
                "valor":valor,
                "saldo":self.saldo,
                "data e tempo":int(time.time),
                })
            return True
        else:
            print(f" O valor {valor} é inválido")
            return False
    def sacar(self, valor):
        """
        método que realiza do depósito na conta bancária.
        Entrada: valor(float)
        return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        """
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({
                "operacao": 0,
                "remetente": self.titular,
                "destinatario": "",
                "valor":valor,
                "saldo":self.saldo,
                "data e tempo":int(time.time()),
                })
            
            print("Saque realizado com sucesso!")
            return True
        else:
            a = input("deseja usar o limite? ({self.limite}) [s para sim]")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    return True
                else:
                    print("Saldo e limite insuficiente!")
            else:
                print("Operação com limite cancelada !")
        return False
    def transferencia(self, conta_destino, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.depositar(valor)
            conta_destino.saldo += valor
            
            self.historico.append({
                "operacao": 2,
                "remetente": self.titular,
                "destinatario": conta_destino.titular,
                "valor": valor,
                "saldo": self.saldo,
                "data e tempo": int(time.time()),
            })
            print("Transferência realizada com sucesso!")
            return True
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            print(f"Valor inválido para transferência: {valor}")
        return False
    
    def exibir_historico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:
            dt = time.localtime(transacao['data e tempo'])
            print("Op: ",transacao['operacao'],
                  "Remetente: ",transacao['remetente'],
                  "Destinatário:", transacao['destinatario'],
                  "Valor: ",transacao['valor'],
                  "Saldo: ",transacao['saldo'], 
                  "Data e Hora: ", str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))