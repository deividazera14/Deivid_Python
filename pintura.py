# Faça um programa que leia a largura e altura de uma parede em metros
# calcule sua area e a quantidade de tinta necessaria  para pinta-la sabendo que cada litro de tinta pinta uma area de 2m²
largura = float(input('qual a largura da sua parede'))
altura = float(input('qual a altura da sua parede'))
area = largura * altura
litros = area/2

print(f'A largura da parede  tem {largura:.2f}\nA altura da parede tem {altura:.2f}\nA area total é {area:.2f}\nPortanto, é necessário {litros:.0f} litros de tinta para pintar a parede,')



