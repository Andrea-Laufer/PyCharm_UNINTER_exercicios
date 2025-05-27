# Escreva um algoritmo que leia um valor e imprima a quantidade de cédulas
# necessárias para esse valor

# cédulas a serem trabalhadas:
# R$ 100
# R$ 50
# R$ 20
# R$ 10
# R$ 5
# R$ 1

print('CAIXA ELETRÔNICO')
print('Cédulas Disponíveis: ')
print('R$ 100')
print('R$ 50')
print('R$ 20')
print('R$ 10')
print('R$ 5')
print('R$ 1')

valor = int(input('Digite o valor em R$ : '))

while True:
    if valor >= 100:
        cont100 = valor // 100
        valor = valor - cont100 * 100
        print(f'Cédulas de 100: {cont100}')
        if not valor:
            break

    if valor >= 50:
        cont50 = valor // 50
        valor = valor - cont50 * 50
        print(f'Cédulas de 50: {cont50}')
        if not valor:
            break

    if valor >= 20:
        cont20 = valor // 20
        valor = valor - cont20 * 20
        print(f'Cédulas de 20: {cont20}')
        if not valor:
            break

    if valor >= 10:
        cont10 = valor // 10
        valor = valor - cont10 * 10
        print(f'Cédulas de 10: {cont10}')
        if not valor:
            break

    if valor >= 5:
        cont5 = valor // 5
        valor = valor - cont5 * 5
        print(f'Cédulas de 5: {cont5}')
        if not valor:
            break

    if valor:
        cont1 = valor
        print(f'Cédulas de 1: {cont1}')
        break




