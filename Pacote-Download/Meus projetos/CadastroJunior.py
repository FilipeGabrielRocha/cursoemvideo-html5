from CMD_UTEIS.lib.cores import *
from CMD_UTEIS.lib.strings import *
from SistemaCadastro.lib.arquivo import *
from SistemaCadastro.lib.interface import *
from time import sleep

arq = 'agendajunior.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas.', 'Cadastrar nova Pessoa.', 'Mandar Mensagem para Contatos', 'Sair do Sistema.'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo.
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resposta == 2:
        #opção para cadastrar um nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        telefone = str(input('Telefone: ')).strip()
        cadastrar(arq, nome, telefone)
    elif resposta == 3:
        #mandar msg para os contatos
        cabecalho('MENSAGEM PARA CONTATOS')
        msg = str(input(f'{digitado_amarelo}Digite sua mensagem aqui: {limpar}')).strip()
        lista_telefo(arq, msg)
    elif resposta == 4:
        #opção para sair do sistema.
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        #digitou um opção errado no menu.
        print(f'{letra_vermelha}ERRO: por favor, digite um número válido!{limpar}')
    sleep(0.5)
