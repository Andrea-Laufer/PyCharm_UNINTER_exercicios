# Escreva um código que permita cadastrar videogames
# informando nome do jogo e a qual videogame pertence
# Construir um menu para cadastrar novo item, listar tudo que foi cadastrado e sair
# Crie uma função para cada item do menu
# Armazene todos os dados em um arquivo txt


def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def existeArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso \n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()



# PROGRAMA PRINCIPAL

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado com sucesso!')
else:
    print('Arquivo inexistente!')
    criarArquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastrar novo item ')
    print('2 - Listar cadastros ')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar selecionada. \n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideogame = input('Nome do Videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada. \n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa')
        break