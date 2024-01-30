from arquivo import *
from time import sleep


arq = 'dadosPessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opcao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # opcao de cadastrar uma pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opcao de sai do sitema.
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida\033[m')
    sleep(2)
