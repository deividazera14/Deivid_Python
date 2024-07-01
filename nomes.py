class Cliente:
    def __init__(self, n, fone, end, ):
        self._nome = n
        self._telefone = fone
        self.endereco = end



    #metodo get (acesso)
    def get_nome(self):
        return self._nome
    #metodo set (acesso)
    def set_nome(self,nome):
         self._nome = nome




    def __str__(self):
        return f" Cliente=(nome,{self._nome} telefone {self._telefone} seu endereço {self.endereco})"
lista_clientes=['luana','232132321', 'rua frei' ]
