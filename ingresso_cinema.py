# cinema cobra preços diferentes de acordo com a idade
# menos de 3 anos de idade, ingresso gratuito
# entre 3 e 12 anos, ingresso custa R$ 15.00
# mais de 12 anos, ingresso custa R$ 30.00

# escreva loop para perguntar a idade do usuário e informar preço ingresso
# encerre o loop qdo usuário digitar 0
# após encerrar loop, informe total de pessoas que compraram ingressos, o valor total pago
# e a média das idades dos compradores

print('CINEMA - Tabela de Preços')
print('Menos de 3 anos - ingresso gratuito')
print('Entre 3 e 12 anos - ingresso R$ 15.00')
print('Mais de 12 anos - ingresso R$ 30.00')
print('Digite 0 para SAIR e encerrar a operação')

total = 0
dinheiro = 0
acc_idades = 0

while True:
    idade = int(input('Digite a sua idade: '))
    if idade == 0:
        break

    total += 1
    acc_idades += idade
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

if total > 0:
    media = acc_idades / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Média idades: {media}')