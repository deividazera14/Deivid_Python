from cliente import Cliente  # Corrigir a importação e colocar no início
from conta import Conta

print('Codando')

c1= Cliente('João','11-9252633', 'rua frei')  # Usar Cliente com C maiúsculo

conta=Conta(c1,1212,0)


conta.depositar(301)
conta.saque(300)
conta.extrato()


print(conta.titular, 'numero',conta.numero,'seu saldo',conta._saldo, )# Corrigir a forma de acessar os atributos

