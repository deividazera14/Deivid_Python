# Crie um programa que jogue jokenpo com o usuario.
import random
import time

resposta =str(input('Vamos jogar jokenpo ? sim/nao'))
while True:
    if resposta in ['sim','s']:
        print('Entao se prepara que vou ganhar de voce lindamente')
        print('\033[32;40m==============================================================\033[m')
        break

    elif resposta in ['nao','n']:
            print('Entao jogamos depois, ate mais! ')
            exit()
usuario=str(input('Escolha uma desssas alternativas:   "Pedra" ,"Papel" ,"Tesoura" !'))

lista= ['pedra','papel','tesoura']

random.shuffle(lista)
lista_embaralhada = lista
maquina=random.choice(lista_embaralhada)

print(f' Estou pensando..... hun ')
time.sleep(2)
print(f'Vou escolher {maquina}')
if usuario == maquina:
    print('Deu Empate ')

elif ((usuario == 'pedra' and maquina == 'tesoura')or \
       (usuario== 'papel' and maquina == 'pedra')or \
       usuario == 'tesoura' and maquina =='papel'):

    print('Ganhei ta facil demais')
    time.sleep(1)
    print('E ainda quer se chamar de Inteligencia Artificial hahahah')

else:
    print('Ganhei de tu usuario Melhore na proxima vez !! kkk')

