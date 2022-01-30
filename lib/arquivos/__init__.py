from lib.interface import leiaInt, c, cabeçalho, linha
import os


def testeArq(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def vazio(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        c('Não foi possível verificar se o arquivo está vazio ou não.', 1)
    else:
        if a.read().strip() == '':
            return True
        else:
            return False
    finally:
        a.close()


def criarArq(arquivo):
    try:
        a = open(arquivo, 'xt')
        a.close()
    except:
        return False
    else:
        return True


def cadastrar(arquivo, idcor=0):
    try:
        nome = str(input(c('Insira o nome do indivíduo ➤ ', idcor, True))).title()
        idade = leiaInt(c('Agora, a idade ➤ ', idcor, True))
        a = open(arquivo, 'at')
        a.write(f'{nome};{idade}\n')
    except:
        c('Não foi possível adicionar essas informações ao sistema, tente novamente.', 1)
    else:
        c(f'Informações de {nome} adicionadas com sucesso.', 5)
    finally:
        a.close()


def excluirArq(arquivo):
    try:
        os.remove(arquivo)
    except (FileExistsError, FileNotFoundError):
        c('O arquivo não foi encontrado ou não existe.', 1)
    else:
        c('Arquivo removido com sucesso.', 5)


def lerArq(arquivo, idcorelem, idcorlinhamenu, idcorletramenu):
    try:
        a = open(arquivo, 'rt')
    except:
        c('Não foi possível ler o arquivo.', 1)
    else:
        print()
        cabeçalho('CADASTROS', idcorletramenu, idcorlinhamenu)
        for line in a:
            elem = line.replace('\n', '').split(';')
            c(f'  {elem[0]:<28}{elem[1]:>5} anos.', idcorelem)
        print()
    finally:
        a.close()
