from Functions import cadastro, registro
vermelho_erro = '\033[1;31m'
fim = '\033[m'

def Menu(str, usuario):
    amarelo_negrito = "\033[1;33m"
    ciano_negrito = "\033[1;36m"
    fim = "\033[m"
    s = '-=' * 60
    # Printa um menu personalizado no terminal
    print(f'{amarelo_negrito}{s}{fim}')
    print(f'{amarelo_negrito}{f"!!BEM - VINDO {usuario.upper()}!!":-^120}{fim}')
    print(f'{amarelo_negrito}{"À":-^120}{fim}')
    print(f'{ciano_negrito}{str:-^120}{fim}')
    print(f'{amarelo_negrito}{s}{fim}')

    print(f'\n{amarelo_negrito}{"Agora resposta as perguntas a seguir..."}{fim}')
    print()


def Janela_principal(book, sheet_cadastro, sheet_admin):
    usuario = []
    admin = 0
    print(f'{"!!Bem-Vindo ao Quiz Seres Mitológicos!!":^100}')
    # Tratamento de ERRO
    while True:
        try:
            forma_login = int(input('\033[4mComo você desseja continuar??\033[m'
                                    '\n1 - \033[34mADMIN\033[m'
                                    '\n2 - \033[97mJOGADOR\033[m'
                                    '\n>> '))
            if forma_login < 1 or forma_login > 2:
                # Caso seja uma opção não válida
                raise ValueError
        except ValueError:
            print(f'{vermelho_erro}[ERRO] Digite uma opção válida.{fim}')
            continue

        else:
            break

    if forma_login == 1:
        usuario = login(sheet_admin)
        admin += 1

    elif forma_login == 2:
        while True:
            try:
                print('\033[4;97m>> JANELA DE JOGADOR\033[m')
                forma_entrada = int(input('1 - JÀ CADASTRADO\n'
                                          '2 - NÃO CADASTRADO\n'
                                          '>> '))
                if forma_entrada < 1 or forma_entrada > 2:
                    # Caso seja uma opção não válida
                    raise ValueError
                elif forma_entrada == 1:
                    usuario = login(sheet_cadastro)

                elif forma_entrada == 2:
                    usuario_cadastro = cadastro(sheet_cadastro)
                    registro(sheet_cadastro, usuario_cadastro, book)
                    continue

            except ValueError:
                print(f'{vermelho_erro}[ERRO] Digite uma opção válida.{fim}')
                continue

            else:
                break

    if admin != 1:
        rank_inicial = 0
        usuario.append(rank_inicial)

    return usuario


def login(sheet):
    usuario = []
    while True:
        # linha para futuramente poder verificar a senha
        linha = 1
        nome_nao_encontrado = 0
        nome_usuario = input('*Nome do Usuário: ').strip()
        for nome in sheet['A']:
            if nome.value == nome_usuario:
                usuario.append(nome.value)
                # nome encontrado, resetando a variavel
                nome_nao_encontrado = 0
                break
            else:
                # nome não compativel
                nome_nao_encontrado += 1
            linha += 1

        if nome_nao_encontrado > 0:
            print(f'{vermelho_erro}[ERRO] Usuário não encontrado.{fim}\n'
                  'Tente novamente.')
            continue
        else:
            while True:
                senha_usuario = input('*Senha do Usuário: ').strip()
                ver_senha_usuario = sheet.cell(row=linha, column=2)
                if ver_senha_usuario.value == senha_usuario:
                    # Usuario existe
                    break
                else:
                    print(f'{vermelho_erro}[ERRO] Senha não compatível com o nome de usuário.{fim}.\n'
                          f'Tente novamente.')
                    continue
            break

    return usuario
