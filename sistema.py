from lib.interface import *
from lib.arquivos import *
passe = 0
arq = 'banco.txt'
while True:
    if passe == 0:
        opmenu = menu('Verificar se o arquivo existe ou está íntegro', 'Sair do programa',
                      corlinha=3, corletras=4, tam=55, corperg=5, dormir=False)
        if opmenu == 1:
            if not testeArq(arq):
                c('O arquivo não foi encontrado ou aberto com sucesso, te levarei ao menu de criação de arquivos.', 1)
                passe = 1
            else:
                c('O arquivo foi aberto com sucesso, te levarei ao menu de manipulação do mesmo.', 5)
                passe = 2
        if opmenu == 2:
            sair()
    if passe == 1:
        opmenu = menu('Criar arquivo', 'Sair do programa',
                      corlinha=3, corletras=4, corperg=5)
        if opmenu == 1:
            if criarArq(arq):
                c('O arquivo foi criado com sucesso, te levarei ao menu de manipulação do mesmo.', 5)
                passe = 2
            else:
                c('O arquivo não foi criado com sucesso, tente novamente.', 1)
                passe = 1
        if opmenu == 2:
            sair()
    elif passe == 2:
        if vazio(arq):
            opmenu = menu('Cadastrar pessoas no sistema', 'Excluir o arquivo', 'Sair do programa',
                          corlinha=3, corletras=4, corperg=5)
            if opmenu == 1:
                cadastrar(arq, 3)
            if opmenu == 2:
                excluirArq(arq)
                passe = 1
            if opmenu == 3:
                sair()
        else:
            opmenu = menu('Listar pessoas já cadastradas', 'Cadastrar pessoas no sistema', 'Excluir o arquivo',
                          'Sair do programa', corlinha=3, corletras=4, corperg=5)
            if opmenu == 1:
                lerArq(arq, 5, 3, 4)
                x = str(input(c('Pressione Enter pra continuar ➤ ', 5, True)))
            if opmenu == 2:
                cadastrar(arq, 3)
            if opmenu == 3:
                excluirArq(arq)
                passe = 1
            if opmenu == 4:
                sair()
