vermelho_erro = '\033[1;31m'
fim = '\033[m'


def remove_caracteres_indesejaveis(cellvalue):
    # função que remove caracteres indesejaveis de uma celula do excel
    import re
    text = re.sub(r"[\r\n\t\x07\x0b]", "", cellvalue)
    return text


# def mostrar_pergunta_respostas(sheet, limite_perg):
#     import re
#     for value in sheet['A']:
#         if value.value == limite_perg:
#             # após achar a pergunta, é agr mostrado na tela.
#             pergunta = sheet.cell(row=limite_perg + 1, column=2)
#             print(f'\033[1;33m{limite_perg}º) {pergunta.value}\033[m')
#             alternativas = sheet.cell(row=limite_perg + 1, column=3)
#             # retira os caracteres indesejáveis
#             alternativas_alterada = remove_caracteres_indesejaveis(alternativas.value)
#             # Formata as alternativas
#             alternativas_lista = re.split('[/]', alternativas_alterada)
#             for alt in alternativas_lista:
#                 print(f"\n   {alt.replace(':', ')')}")
#             print('')
#
#         else:
#             pass


def guarda_perguntas(sheet, limite_perg):
    import re
    # Cria uma lista que vai receber todas as perguntas da planilha
    perguntas = []
    alternativas_corretas = []
    # percorre todas as linhas que terão perguntas
    for row in sheet.iter_rows(min_row=2, max_row=limite_perg + 1):
        pergunta = {}
        perg = []
        for cell in row:
            # colocara cada pergunta em uma variavel
            perg.append(cell.value)
        # após colocará os valores em suas devidas variaveis para depois retornalas.
        pergunta['Questão'] = perg[1]
        alternativas = perg[2]
        alternativas_alterada = remove_caracteres_indesejaveis(alternativas)
        alternativas_lista = re.split('[/]', alternativas_alterada)
        pergunta['Alternativas'] = alternativas_lista
        alternativas_corretas.append(perg[3])
        perguntas.append(pergunta)

    return perguntas, alternativas_corretas


def printa_pergunta(perguntas, index):
    # printa a pergunta baseado no valor aleatorio gerado
    print(f'{index + 1}º) {perguntas[index]["Questão"]}')

    for alt in perguntas[index]['Alternativas']:
        print(f"  {alt.replace(':', ')')}")


def verificar_resposta(alternativas, index, rep, sheet):
    # verifica a resposta do usuario com a resposta correta
    resposta_correta = alternativas[index]
    # Determinando a dificuldade da pergunta, sendo ela dificil(2) ou facil(1)
    dificuldade = 0
    if sheet.cell(row=index+2, column=5).value == 'dificil':
        # Pergunta dificil
        dificuldade += 2
    elif sheet.cell(row=index+2, column=5).value == 'fácil':
        # Pergunta facil
        dificuldade += 1

    return dificuldade if resposta_correta == rep else 0


def cadastro(sheet):
    # cadastro de usuario
    usuario = []
    # coleta de dados
    while True:
        # Variavel para servir como verificação de nome
        nome_valido = 0
        nome = input('*Cadastro de usuario: ').strip()

        # loop para verificar se o usuario já foi cadastrado
        for n in sheet['A']:
            if nome == n.value:
                print(f'{vermelho_erro}Usuário já registrado!{fim}')
                nome_valido += 1
                break

        if nome_valido > 0 or len(nome) < 3:
            # caso o usuario já foi cadastrado ou é muito curto
            print('O nome do usuário é muito curto ou já esta sendo ultilizado.\n'
                  'Tente novamente.')
            continue
        else:

            usuario.append(nome)
            while True:
                # coleta da senha
                senha = input('*Cadastro de senha: ').strip()
                if len(senha) < 6:
                    print('A senha deve conter no minimo 6 caracteres.')
                    continue
                else:
                    usuario.append(senha)
                    break
        break

    return usuario


def registro(sheet, usuario, book):
    sheet.append(usuario)
    book.save('C:\\Users\\orian\\PycharmProjects\\QuizGame2.0\\Pasta1.xlsx')
