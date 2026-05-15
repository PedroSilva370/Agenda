from time import sleep as sl
agenda = list()
# Funções
def adicionar_compromisso():
    """
    -> Função que serve para adicionar um compromisso a sua lista.
    :return: adiciona um dicionario para a lista agenda
    """
    compromisso = dict()
    compromisso['titulo'] = input('\nTitulo: ')
    compromisso['data'] = input('Data: ')
    resp = str(input('Tem hora marcada? [S/N] ')).strip().lower()
    while True:
        if resp == 's':
            compromisso['hora'] = input('Hora: ')
            break
        elif resp == 'n':
            compromisso['hora'] = 'Sem hora marcada'
            break
        else:
            print('ERRO! Digite somente S ou N.')
    agenda.append(compromisso)
def ver_agenda():
    """
    -> Função que serve para ver qual compromisso está dentro da agenda.
    :return: a lista printada de forma organizada.
    """
    if len(agenda) == 0:
        print('Nenhum compromisso encontrado!')
    else:
        print(f'{"ID"} \t{"Titulo"} \t{"Data":^5} \t{"Hora"}')
        print('---------------------------------------')
        for k, v in enumerate(agenda):
            print(f"{k} \t{v['titulo']}  \t{v['data']:^5}  \t{v['hora']}")

def editar_compromisso():
    """
    -> Função para editar os compromissos.
    :return: o compromissos editados.
    """
    if len(agenda) == 0:
        print('Nenhum compromisso encontrado!')
    else:
        resp = int(input("Qual o id do compromisso: ").strip())

        for k, v in enumerate(agenda):
            if k == resp:
                v['titulo'] = input('\nTitulo: ')
                v['data'] = input('Data: ')

                while True:
                    hora = input('Tem hora marcada? [S/N] ').strip().lower()

                    if hora == 's':
                        v['hora'] = input('Hora: ')
                        break

                    elif hora == 'n':
                        v['hora'] = 'Sem hora marcada'
                        break

                    else:
                        print('ERRO! Digite somente S ou N.')

                print('Compromisso editado com sucesso!')
                break

def remover_compromisso():
    """
    -> Função que serve para remover um compromisso da agenda.
    :return: remove o compromisso dentro da lista agenda.
    """
    resp = str(input("Qual o id do compromisso: ")).strip()
    resp = int(resp)
    for k, v in enumerate(agenda):
        if k == resp:
            certeza = input('Você tem certeza que deseja remover? [S/N] ').strip().lower()
            if certeza == 's':
                agenda.pop(k)
            elif certeza == 'n':
                print('Cancelando... ')
def busca():
    """
    -> Função que busca pelo id o compromisso.
    :return: somente o compromisso desejado.
    """
    if len(agenda) == 0:
        print('Nenhum compromisso encontrado!')
    else:
        resp = str(input("Qual o id do compromisso: ")).strip()
        resp = int(resp)
        for k, v in enumerate(agenda):
            if k == resp:
                print(f'\n{"ID":^3} {"Titulo":^7} {"Data":^6} {"Hora":^7}')
                print('---------------------------------------')
                print(f"{v['titulo']:^7}  {v['data']:^6}  {v['hora']:^7}")
                print('---------------------------------------')
            else:
                print('Compromisso não encontrado.')
def sair():
    print('\nSaindo...')
    sl(1)
    print('<<< VOLTE SEMPRE >>>')
    exit()
# ENTRADA
def escreva(msg):
    """
    -> Função que printa um titulo.
    :param msg: mensagem desejada.
    :return:
    """
    tam = len(msg) + 4
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
escreva('Bem-Vindo a sua Agenda!')
sl(1)
try:
    while True:
        menu = int(input('''\nO que você deseja fazer:
[ 1 ] Adicionar compromisso
[ 2 ] Ver agenda
[ 3 ] Editar compromisso
[ 4 ] Remover compromisso
[ 5 ] Buscar por ID
[ 0 ] Sair
: '''))

        # PROCESSAMENTO
        if menu == 1:
            adicionar_compromisso()
        elif menu == 2:
            ver_agenda()
        elif menu == 3:
            editar_compromisso()
        elif menu == 4:
            remover_compromisso()
        elif menu == 5:
            busca()
        elif menu == 0:
            sair()
        else:
            print('Você digitou o número errado.')
except ValueError:
    print('Erro! Valor inválido.')
    print('Recomece o programa.')
except Exception:
    print('Erro! Houve um erro.')
    print('Recomece o programa.')
