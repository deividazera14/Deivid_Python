# triangulo equilatero sao aqueles q todos os lados sao iguais
# Triangulo esosceles sao aqueles q tem dois lados iguais
# Triangulo escaleno é aquele que todos os lados sao diferentes mas formam um triangulo

a = float(input('Digite o parametro A '))
b = float(input('Digite o parametro B '))
c = float(input('Digite o parametro C '))




if a + b > c and a + c > b and b + c > a:

# condiçoes para forma um trinagulo.
    if a == b == c:
        print('todos os lados sao iguais e formam um triangulo Equilatero')

    elif a == b or b == c or c == a:
        print('Dois parametro é iguais e podem forma um triangulo esosceles')

    else:
        print('Os 3 valores sao diferentes entao forma um triangulo escaleno')

else:
    print('nao podem forma um triangulo')