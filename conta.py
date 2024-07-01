class Conta:
    def __init__(self, titular, numero, valor= 0, ):
        self._saldo = valor
        self.numero =numero
        self.titular=titular



    def depositar(self,valor):
        self._saldo+=valor

    def saque(self,valor):
        if (self._saldo>=valor):
            self._saldo-=valor
            print('saque realizado com sucesso')
        else:
            print('saldo insuficiente')

    def extrato (self):
        print(f' titular da conta,{self.titular} e o seu novo saldo é {self._saldo}')


    #A função Property deve ser utilizada somente se você precisar da funcionalidade de transformar
    #ou verificar um atributo quando ele é atribuído ou lido.
    def get_saldo(self):
        return self._saldo

    def set_saldo(self,saldo):
        if saldo <0 :
            print('seu saldo nao pode ser negativo')
        else:
            self._saldo=saldo


