# condiçao da saida do jogo é se o usuario perde e assim mostrar quantas sequencias de vitoria teve  

import random

print('▬'*20)
print(f'\033[1m VAMOS JOGAR PAR OU IMPAR \033[m!\U0001F3AE ')
maquina=random.randint(1,10)
print('▬'*20)

vitoria = 0
perdeu= 0
while True:
    jogador = int(input('Digite um valor'))
    escolha = str(input('Escolha Par ou Impar '))

    total= jogador+maquina

    if escolha =='par':
        if total %2==0:
            vitoria+=1
            print('\033[35m=\033[0m' * 49)
            print('\033[32m Voce venceu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Par')
            print('Vamos jogar de novo !')
            print('\033[35m=\033[0m' * 49)
        else:
            print('\033[35m=\033[0m' * 49)
            print('\033[31m Voce perdeu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Impar')
            print('\033[35m=\033[0m' * 49)
            break

    elif escolha == 'impar':
        if total %2!=0:
            vitoria+=1
            print('\033[35m=\033[0m' * 49)
            print('\033[32m Voce venceu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Impar')
            print('Vamos jogar de novo !')
            print('\033[35m=\033[0m' * 49)
        else:
            print('\033[35m=\033[0m' * 49)
            print('\033[31m Voce perdeu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Par')
            print('\033[35m=\033[0m' * 49)
            break

    elif total %2==0:
        if maquina %2==0:
            perdeu+=1
            print('\033[35m=\033[0m' * 49)
            print('\033[31m Voce perdeu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Par')
            print('\033[35m=\033[0m' * 49)
            break
        else:  # precisava por o else caso o usuario ganhace da maquina
            print('\033[35m=\033[0m' * 49)
            print('\033[32m Voce venceu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Impar')
            print('\033[35m=\033[0m' * 49)
    else:
        if maquina %2!=0 :  #essa linha teria quer ter colocar dessa forma mesmo pois se a maquina fosse escolher impar teria quer ser a negaçao do par
            perdeu+=1

            print('=' * 49)
            print('\033[31m Voce perdeu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Impar')
            print('=' * 49)
            break
        else:
            print('\033[35m=\033[0m' * 49)
            print('\033[32m Voce venceu \033[m')
            print(f'Voce escolheu {jogador}, maquina {maquina} e a soma é {total} deu Par')
            print('\033[35m=\033[0m' * 49)

print(f'O total de vezes que voce ganhou foi --> {vitoria} \U0001F3C6 <--')
