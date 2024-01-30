from interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # O comando open() e para abrer o arquivo
        a.close()  # O comando close() e para feicha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # O comando open() e para abrer o arquivo
        a.close()  # O comando close() e para feicha o arquivo
    except:
        print('\033[31mHove um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criando com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')  # O comando open() e para abrer o arquivo
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRODAS')
        for linha in a:
            dado = linha.split(';')  # O comando split() e para separa ou dividi por ponto e virgola
            dado[1] = dado[1].replace('\n', '')  # O comando replace() e para subistitui \n por ''
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # o :<30 e para alinhar o nome com 30 carequiteres linhada a esqueda
        # O comando e para ler o arquivo e nostrar
    finally:
        a.close()  # O comando close() e para feicha o arquivo


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # O comando open() e para abrer o arquivo
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # o comando write() e para escrever o dado no arquivo
        except:
            print('Houve um ERRO na hora de escrever as dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()  # O comando close() e para feicha o arquivo
