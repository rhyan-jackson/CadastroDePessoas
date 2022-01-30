from time import sleep
cores = [
    '\033[m',  # 0 ➤ limpa
    '\033[31m',  # 1 ➤ vermelho
    '\033[33m',  # 2 ➤ amarelo
    '\033[34m',  # 3 ➤ azul escuro
    '\033[36m',  # 4 ➤ azul claro
    '\033[32m',  # 5 ➤ verde
]


def c(msg, idcor=0, retorna=False):
    if retorna:
        return f'{cores[idcor]}{msg}{cores[0]}'
    else:
        print(f'{cores[idcor]}{msg}{cores[0]}')


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            c('Insira somente números inteiros.', 1)
        else:
            return a


def linha(cor=0, tam=42):
    c('-' * tam, cor)


def cabeçalho(msg, corletras=0, corlinha=0, tam=42):
    linha(corlinha, tam)
    c(msg.center(tam), corletras)
    linha(corlinha, tam)


def menu(*opções, corletras=0, corlinha=0, corperg, tam=42, dormir=True):
    if dormir:
        sleep(2)
    cabeçalho('MENU PRINCIPAL', corletras, corlinha, tam)
    for ordem, i in enumerate(opções):
        print(c(f'{ordem + 1} ➤ {i}', corletras, True), end='')
        print(c(';', corlinha, True) if ordem != len(opções) - 1 else c('.', corlinha, True))
    linha(corlinha, tam)
    while True:
        a = leiaInt(c('Selecione uma opção dentre as fornecidas ➤ ', corperg, True))
        if 1 <= a <= len(opções):
            return a
        else:
            c('Insira somente um número dentre as opções acima.', 1)


def sair():
    c('Saindo do programa, obrigado por ter utilizado nossos serviços.', 1)
    exit()
