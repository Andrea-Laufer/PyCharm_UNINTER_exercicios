# Escreva uma função que calcule o fatorial de um número recebido como parâmetro
# Retorne o resultado
# Valide os dados por outra função, de modo que sejam aceitos apenas valores positivos
# Crie o help da função
from matplotlib.rcsetup import validate_int

'''
    Função para validar o valor que terá o fatorial calculado.
'''

def valida_int (pergunta, min, max):

    '''

    :param pergunta: número inteiro a ser calculado.
    :param min: 0
    :param max: 99999
    :return: só sai do laço while se o valor digitado for > 0 e < 99999
    '''

    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def fatorial (num):

    '''
    Função Fatorial
    :param num: valor a ser fatoriado
    :return: resultado da fatorial de num
    '''

    fat = 1
    if num == 0:
        return fat
    for i in range (1, num + 1, 1):
        fat *= i
    return fat


x = valida_int('Digite um valor para calcular o fatorial: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')

help(valida_int)
help(fatorial)

print(help(fatorial))
print(help(valida_int))