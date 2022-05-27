def menu_admin(str):
    print('-=' * 60)
    print(f'{"PAINEL DE CONTROLE_QUIZ":-^120}')
    print(f'::\033[4m{str}\033[m::')
    print('>> O que deseja fazer:\n'
          '     1 - ADICIONAR UMA QUESTÃO\n'
          '     2 - REMOVER UMA QUESTÃO\n'
          '     3 - VISUALIZAR TODAS AS QUESTÕES\n'
          '     4 - SAIR')


def adcionar_pergunta(sheet, book, perguntas, alternativas_corretas):
    rows = sheet.max_row
    from time import sleep
    pergunta = []
    # Adiciona a número da questão
    pergunta.append(rows)
    # Cria uma variavel que vai receber a pergunta.
    questao = input('Como será a questão que deseja adicionar:\n'
                    '>> ').capitalize().strip()
    pergunta.append(questao)
    while True:
        # Se continuar em 0 então as alternativas foram feitas do jeito desejado.
        formatacao = 0
        alternativas = input('Quais são as alternativas para essa questão:\n'
                             'SIGA O MODELO PADRÃO PARA ALTERNATIVAS == \033[1;4mA:ALT/B:ALT/C:ALT\033[m\n'
                             '>> ').strip()

        # Verifica se as alternaativas foi formatada da maneira que foi desejada, senão,
        # será necessário refazer as alternativas
        for a in range(0, len(alternativas)):
            if alternativas[0] == 'A':
                if alternativas[1] != ':':
                    formatacao += 1
                    break

            elif alternativas[a-1] == '/' and alternativas[a] in 'BC' and alternativas[a+1] == ':':
                pass

            else:
                formatacao += 1
                break

        if formatacao > 0:
            continue

        else:
            pergunta.append(alternativas)
            break
    # Pega o a resposta correta para a pergunta criada
    while True:
        alternativas_correta = input('Qual a alternativa correta para essa pergunta:\n'
                                     '>> ').strip().upper()

        if alternativas_correta not in 'ABC' or alternativas_correta == '':
            print('Por favor digite uma alternativa válida.\n'
                  'Tente novamente.')
            continue

        else:
            pergunta.append(alternativas_correta)
            break
    # Define a dificuldade da pergunta criada
    while True:
        dificuldade = input('Qual a dificuldade para essa pergunta que vai ser adcionada:\n'
                            '>> ').strip().lower()

        if dificuldade == 'dificil' or dificuldade == 'fácil':
            pergunta.append(dificuldade)
            break

        else:
            print('As dificuldades possiveis são fáceis ou difíceis.\n'
                  'Tente novamente.')
            continue

    # Adciona a pergunta na planilha
    sheet.append(pergunta)
    print('Salvando pergunta...')
    sleep(1)
    book.save('C:\\Users\\orian\\PycharmProjects\\QuizGame2.0\\Pasta1.xlsx')
    pergunta_dic = {}
    pergunta_dic["Questão"] = questao
    pergunta_dic['Alternativas'] = alternativas
    perguntas.append(pergunta_dic)
    alternativas_corretas.append(alternativas_correta)
    print('Pergunta salva.')


def remover_pergunta(sheet, book):
    from time import sleep
    rows = sheet.max_row
    while True:
        try:
            pergunta = int(input('Qual o número da pergunta que deseja remover:\n'
                                 '>> '))
            if pergunta > rows - 1:
                # Caso se digite uma pergunta que não existe
                raise ValueError

            else:
                print('Removendo pergunta...')
                sleep(1)
                sheet.delete_rows(pergunta + 1)

        except ValueError:
            print('\033[1;31m[ERRO] Por favor digite uma pergunta válida.\033[m\n'
                  'Tente novamente.')
            continue

        else:
            break

    # Salvando processo
    print('Salvando planilha...')
    sleep(1)
    book.save('C:\\Users\\orian\\PycharmProjects\\QuizGame2.0\\Pasta1.xlsx')
    print('Alteração salva.')
