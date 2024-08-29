numero = int(input('Escolha um numero'))
numero2 = int(input('Escolha um numero'))
menu= False
soma= numero+numero2
multiplicar = numero*numero2
maior= max(numero,numero2)
novos_numeros= None
sair = None

while not menu:
    escolha=int(input(f"""Escolha uma dessas opções !'
Opção 1 = soma
Opção 2 = multiplicar
Opção 3 = maior
Opção 4 = novos_numeros
Opção 5 = sair """))

    if escolha == 1:
        print(f'Opção 1 Atendida: Valor da soma é {soma}')
        break
    elif escolha == 2:
        print(f'Opção 2 Atendida: valor da multiplicação é {multiplicar}')
        break
    elif escolha == 3:
        print(f'Opção 3 Atendida: valor do maior numero é {maior}')
        break
    elif escolha == 4:
        novo= int(input('Digite um novo numero'))
        d = int(input('Digite mais um numero'))
        soma= novo+d
        multi =novo*d
        maior= max(novo,d)
        entrada = int(input("""Qual dessas opções vc prefere ?'
        Opção 1= soma
        Opção 2= multi
        Opção 3= maior """ ))
        if entrada == 1:
            print(soma)
            break
        elif entrada == 2:
            print(multi)
            break
        elif entrada == 3:
            print(maior)
            break
    elif escolha == 5 :
        print('Ate mais tarde Bye Bye')
        exit()
    else:
        print('Opção inesxistente tente novamente')






