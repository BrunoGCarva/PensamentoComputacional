import time
class ContaCorrente:
    """
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular(str), saldo(float), limite(float), historico(lista de dicionários)
    
    OBS: Operações no histórico: 0 - sacar, 1- depositar, 2 - transferir
    """
    
    def __init__(self,titular:str, saldo:float, limite:float,historico:list)->None:
        """
        Construtor da classe CntaBancária
        """
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = historico
    def __str_(self):
        return f"Titular: {self.__titular}, Saldo: {self.__saldo}, Limite: {self.__limite}"
    def depositar(self, valor:float, remetente:str = None) -> bool:
        """
        método que realiza do depósito na conta bancária.
        Entrada: valor(float), destinatário (Str) 
        return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        """
        op= 1
        if remetente != None:
            op = 2
        if valor > 0:
            self.__saldo += valor
            self.__historico.append({
                "operacao": op,
                "remetente": remetente,
                "destinatario": self.__titular,
                "valor":valor,
                "saldo":self.__saldo,
                "data e tempo":int(time.time()),
                })
            return True
        else:
            print(f" O valor {valor} é inválido")
            return False
    def sacar(self, valor:float, destinatario:str = None)->bool:
        """
        método que realiza do depósito na conta bancária.
        Entradas: valor(float) e destinatário (Str)
        return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        """
        op = 0
        if destinatario != None:
            op = 2
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append({
                "operacao": 0,
                "remetente": self.__titular,
                "destinatario": destinatario,
                "valor":valor,
                "saldo":self.__saldo,
                "data e tempo":int(time.time()),
                })
            
            print("Saque realizado com sucesso!")
            return True
        else:
            a = input("deseja usar o limite? ({self.___limite}) [s para sim]")
            if a == 's':
                if (self.__saldo + self.___limite) >= valor:
                    self.__saldo -= valor
                    return True
                else:
                    print("Saldo e limite insuficiente!")
            else:
                print("Operação com limite cancelada !")
        return False
    def transferir(self, destinatario:str, valor:float)->bool:
        """
        Objetivo: método para transferir um valor entre duas contas.
        Entradas: valor (float) e obj do destinatário
        Saída: True se ok, False se NOK
        """
        if self.sacar(valor, destinatario.titular):
            destinatario.depositar(valor, self.__titular)
        
        
    def exibir_historico(self)->None:
        print("Histórico de Transações:")
        for transacao in self.__historico:
            dt = time.localtime(transacao['data e tempo'])
            print("Op: ",transacao['operacao'],
                  "Remetente: ",transacao['remetente'],
                  "Destinatário:", transacao['destinatario'],
                  "Valor: ",transacao['valor'],
                  "Saldo: ",transacao['saldo'], 
                  "Data e Hora: ", str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))
            