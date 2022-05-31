import os

def jogar_perguntaResposta():
    os.system("cls")
    print("\n*********************************")
    print("Bem vindo ao jogo Perguntas e Respostas!!")
    print("*********************************")
    try:
        nome = str(input('\nDigite o nome do participante: '))
    except ValueError:
        print('Nome Invalido')
    else:
        try:
            print('\nSELECIONE AS MATÉRIAS')
            categoria = (
                '{1} -> Matemática',
                '{2} -> Ciências',
                '{3} -> Inglês',
                '{4} -> Espanhol',
                '{5} -> Todas as matérias',
            )
            for loop in categoria:
                print(loop)

            escolha_materias = int(input())
            if escolha_materias == 1:
                os.system("cls")
                print(f'\nMuito bem {nome}, vamos ao game!')
                print('\nQuanto é a metade de 6, mais 6 ?')
                pergunta1 = (
                    '[1] -> 3',
                    '[2] -> 6',
                    '[3] -> 9',
                    '[4] -> 12',
                )
                for loop in pergunta1:
                    print(loop)

                select_questao1 = int((input()))

                if select_questao1 == 3:
                    os.system("cls")
                    print('\nCerta resposta!')
                    print('\nPara calcular a potência de potência de mesma base, conserva a base e...')
                    pergunta2 = (
                        '[1] -> Multiplico os expoentes.',
                        '[2] -> Divido os expoentes.',
                        '[3] -> Somo os expoentes.',
                        '[4] -> Subtraio os expoentes.',
                    )
                    for loop in pergunta2:
                        print(loop)

                    select_questao2 = int(input())

                    if select_questao2 == 1:
                        os.system("cls")
                        print('\nCerta Resposta!')
                        print('\nBilionésimo é um número ordinal equivalente a: ')
                        pergunta3 = (
                            '[1] -> Milhar',
                            '[2] -> Bilhão',
                            '[3] -> Milhão',
                            '[4] -> Trilhão',
                        )
                        for loop in pergunta3:
                            print(loop)

                        select_questao3 = int(input())

                        if select_questao3 == 2:
                            os.system("cls")
                            print('\nCerta Resposta!')
                            print('\nSomando a minha idade com a de meu irmão, obtenho 22 anos. Com quanto dara a soma'
                                  ' de nossas idades daqui a 3 anos?')
                            pergunta4 = (
                                '[1] -> 25 anos',
                                '[2] -> 26 anos',
                                '[3] -> 28 anos',
                                '[4] -> 30 anos',
                            )
                            for loop in pergunta4:
                                print(loop)

                            select_questao4 = int(input())

                            if select_questao4 == 3:
                                os.system("cls")
                                print('\nCerta Resposta!')
                                print('\nSegundo a regra, o módulo é sempre um número real: ')
                                pergunta5 = (
                                    '[1] -> Não negativo',
                                    '[2] -> Menores que zero',
                                    '[3] -> Menos Infinito',
                                    '[4] -> Negativo',
                                )
                                for loop in pergunta5:
                                    print(loop)

                                select_questao5 = int(input())

                                if select_questao5 == 1:
                                    os.system("cls")
                                    print('\nCerta Resposta!')
                                    print('\nQual é o número seguinte na sequência 421, 332, 243...?')
                                    pergunta6 = (
                                        '[1] -> 152',
                                        '[2] -> 153',
                                        '[3] -> 154',
                                        '[5] -> 155',
                                    )
                                    for loop in pergunta6:
                                        print(loop)

                                    select_questao6 = int(input())

                                    if select_questao6 == 3:
                                        os.system("cls")
                                        print('\nCerta Resposta!')
                                        print('\nQual destes números não é racional: ')
                                        pergunta7 = (
                                            '[1] -> 0,333333...',
                                            '[2] -> -251',
                                            '[3] -> 2/7',
                                            '[4] -> Raiz Quadrara de 2',
                                        )
                                        for loop in pergunta7:
                                            print(loop)

                                        select_questao7 = int(input())

                                        if select_questao7 == 4:
                                            os.system("cls")
                                            print('\nCerta Resposta!')
                                            print('\nQual número é maior que 7?')
                                            pergunta8 = (
                                                '[1] -> 12',
                                                '[2] -> 3',
                                                '[3] -> 5',
                                                '[4] -> 2',
                                            )
                                            for loop in pergunta8:
                                                print(loop)

                                            select_questao8 = int(input())

                                            if select_questao8 == 1:
                                                os.system("cls")
                                                print('\nCerta Resposta!')
                                                print('\nQuantas unidades encontramos em duas dúzias?')
                                                pergunta9 = (
                                                    '[1] -> 10',
                                                    '[2] -> 12',
                                                    '[3] -> 20',
                                                    '[4] -> 24',
                                                )
                                                for loop in pergunta9:
                                                    print(loop)

                                                select_questao9 = int(input())

                                                if select_questao9 == 4:
                                                    os.system("cls")
                                                    print('\nCerta Resposta!')
                                                    print('\nO resultado da expressão 2 + 5 * 9 é:')
                                                    pergunta10 = (
                                                        '[1] -> 47',
                                                        '[2] -> 63',
                                                        '[3] -> 23',
                                                        '[4] -> 40',
                                                    )
                                                    for loop in pergunta10:
                                                        print(loop)

                                                    select_questao10 = int(input())

                                                    if select_questao10 == 1:
                                                        os.system("cls")
                                                        print('\nCerta Resposta!')
                                                        print(f'\nPARABENS {nome.upper()} VOCÊ ACERTOU TODAS AS '
                                                              f'PERGUNTAS')
                                                        input()
                                                    else:
                                                        print('\nResposta Errada')
                                                        input()
                                                else:
                                                    print('\nResposta Errada')
                                                    input()
                                            else:
                                                print('\nResposta Errada')
                                                input()
                                        else:
                                            print('\nResposta Errada')
                                            input()
                                    else:
                                        print('\nResposta Errada')
                                        input()
                                else:
                                    print('\nResposta Errada')
                                    input()
                            else:
                                print('\nResposta Errada')
                                input()

                        else:
                            print('\nResposta Errada')
                            input()

                    else:
                        print('\nResposta Errada')
                        input()

                else:
                    print('\nResposta Errada!')
                    input()

            elif escolha_materias == 2:
                os.system("cls")
                print(f'\nMuito bem {nome}, vamos ao game!')
                print('\nNo corpo Humano, onde se localiza o pâncreas?')
                pergunta1 = (
                    '[1] -> No Abdome',
                    '[2] -> Nas Pernas',
                    '[3] -> Na Cabeça',
                    '[4] -> Nos Braços',
                )
                for loop in pergunta1:
                    print(loop)

                select_questao1 = int(input())

                if select_questao1 == 1:
                    os.system("cls")
                    print('\nCerta Resposta')
                    print('\nQue doença é frequentemente transmitida por água poluída?')
                    pergunta2 = (
                        '[1] -> Raiva',
                        '[2] -> Febre Tifóide',
                        '[3] -> Resfriado',
                        '[4] -> Malaria',
                    )
                    for loop in pergunta2:
                        print(loop)

                    select_questao2 = int(input())

                    if select_questao2 == 2:
                        os.system("cls")
                        print('\nCerta Resposta.')
                        print('\nA adição de saliva ao bolo alimentar constitui aquilo que chamamos de:')
                        pergunta3 = (
                            '[1] -> Salivação',
                            '[2] -> Ensalivação',
                            '[3] -> Deglutição',
                            '[4] -> Digistão',
                        )
                        for loop in pergunta3:
                            print(loop)

                        select_questao3 = int(input())

                        if select_questao3 == 2:
                            os.system("cls")
                            print('\nCerta Resposta')
                            print('\nJugular é algo pertencente...')
                            pergunta3 = (
                                '[1] -> a garganta',
                                '[2] -> ao ouvido',
                                '[3] -> ao peito',
                                '[4] -> aos pés',
                            )
                            for loop in pergunta3:
                                print(loop)

                            select_questao3 = int(input())

                            if select_questao3 == 1:
                                os.system("cls")
                                print('\nCerta Resposta')
                                print('\nAo emborcar um ponte de vidro sobre uma vela acesa, ela se apaga por '
                                      'falta de: ')
                                pergunta4 = (
                                    '[1] -> Espaço',
                                    '[2] -> Oxigênio',
                                    '[3] -> Gas Carbônico',
                                    '[4] -> Poeira',
                                )
                                for loop in pergunta4:
                                    print(loop)

                                select_questao4 = int(input())

                                if select_questao4 == 2:
                                    os.system("cls")
                                    print('\nCerta Resposta')
                                    print('\nComo se chama o estado da água na forma de gelo?')
                                    pergunta5 = (
                                        '[1] -> Sólido',
                                        '[2] -> Líquido',
                                        '[3] -> Vapor',
                                        '[4] -> Normal',
                                    )
                                    for loop in pergunta5:
                                        print(loop)

                                    select_questao5 = int(input())

                                    if select_questao5 == 1:
                                        os.system("cls")
                                        print('\nCerta Resposta')
                                        print('\nO Bacu-de-Pedra é uma espécie de qué?')
                                        pergunta6 = (
                                            '[1] -> Aracnídeo',
                                            '[2] -> Mamífero',
                                            '[3] -> Peixe',
                                            '[4] -> Ave',
                                        )
                                        for loop in pergunta6:
                                            print(loop)

                                        select_questao6 = int(input())

                                        if select_questao6 == 3:
                                            os.system("cls")
                                            print('\nCerta Resposta')
                                            print('\nO que é Macuco?')
                                            pergunta7 = (
                                                '[1] -> Peixe',
                                                '[2] -> Macaco',
                                                '[3] -> Caipira',
                                                '[4] -> Ave',
                                            )
                                            for loop in pergunta7:
                                                print(loop)

                                            select_questao7 = int(input())

                                            if select_questao7 == 4:
                                                os.system("cls")
                                                print('\nCerta Resposta')
                                                print('\nQual desses animais é muito resistente a falta de água'
                                                      ', calor e a fadiga?')
                                                pergunta8 = (
                                                    '[1] -> Camelo',
                                                    '[2] -> Cavalo-Marinho',
                                                    '[3] -> Bagre',
                                                    '[4] -> Bonsai',
                                                )
                                                for loop in pergunta8:
                                                    print(loop)

                                                select_questao8 = int(input())

                                                if select_questao8 == 1:
                                                    os.system("cls")
                                                    print('\nCerta Resposta')
                                                    print('\nQual das seguintes é uma fonte de energética renovável? ')
                                                    pergunta9 = (
                                                        '[1] -> Energia eólica',
                                                        '[2] -> Gás Natural',
                                                        '[3] -> Petróleo',
                                                        '[4] -> Carvão mineral',
                                                    )
                                                    for loop in pergunta9:
                                                        print(loop)

                                                    select_questao9 = int(input())

                                                    if select_questao9 == 1:
                                                        os.system("cls")
                                                        print('\nCerta Resposta')
                                                        print('\nQual é o maior planeta do Sistema Solar?')
                                                        pergunta10 = (
                                                            '[1] -> Netuno',
                                                            '[2] -> Júpiter',
                                                            '[3] -> Vênus',
                                                            '[4] -> Saturno',
                                                        )
                                                        for loop in pergunta10:
                                                            print(loop)

                                                        select_questao10 = int(input())

                                                        if select_questao10 == 2:
                                                            os.system("cls")
                                                            print('\nCerta Resposta')
                                                            print(f'\nPARABENS {nome.upper()} VOCÊ ACERTOU TODAS AS '
                                                                  f'PERGUNTAS')
                                                            input()
                                                        else:
                                                            print('\nResposta Errada!')
                                                            input()
                                                    else:
                                                        print('\nResposta Errada!')
                                                        input()
                                                else:
                                                    print('\nResposta Errada!')
                                                    input()
                                            else:
                                                print('\nResposta Errada!')
                                                input()
                                        else:
                                            print('\nResposta Errada!')
                                            input()
                                    else:
                                        print('\nResposta Errada!')
                                        input()
                                else:
                                    print('\nResposta Errada!')
                                    input()
                            else:
                                print('\nResposta Errada!')
                                input()
                        else:
                            print('\nResposta Errada!')
                            input()
                    else:
                        print('\nResposta Errada!')
                        input()
                else:
                    print('\nResposta Errada!')
                    input()

            elif escolha_materias == 3:
                os.system("cls")
                print(f'\nMuito bem {nome}, vamos ao game!')
                print('\nEm inglês, que tempo verbal se usa para indicar uma ação que esta acontecendo'
                      'agora?')
                pergunta1 = (
                    '[1] -> Simple Present',
                    '[2] -> Present Continuos',
                    '[3] -> Present Perfect',
                    '[4] -> Simple Past',
                )
                for loop in pergunta1:
                    print(loop)

                select_questao1 = int(input())

                if select_questao1 == 2:
                    os.system("cls")
                    print('\nCerta Resposta.')
                    print('\nChoose the correct answer. Only at night __________ the safety of their cave. ')
                    pergunta2 = (
                        '[1] -> Bats Leave',
                        '[2] -> Leave bats',
                        '[3] -> Bats Will Leave',
                        '[4] -> Do Bats Leave',
                    )
                    for loop in pergunta2:
                        print(loop)

                    select_questao2 = int(input())

                    if select_questao2 == 1:
                        os.system("cls")
                        print('\nCerta Resposta.')
                        print('\nQual dessas alternativas não corresponde a um tipo de animal ?')
                        pergunta2 = (
                            '[1] -> Cat',
                            '[2] -> Clown',
                            '[3] -> Giraff',
                            '[4] -> Duck',
                        )
                        for loop in pergunta2:
                            print(loop)

                        select_questao2 = int(input())

                        if select_questao2 == 2:
                            os.system("cls")
                            print('\nCerta Resposta.')
                            print('\nQual animal não é um inseto?')
                            pergunta3 = (
                                '[1] -> Ant',
                                '[2] -> Bee',
                                '[3] -> Fly',
                                '[4] -> Horse',
                            )
                            for loop in pergunta3:
                                print(loop)

                            select_questao3 = int(input())

                            if select_questao3 == 4:
                                os.system("cls")
                                print('\nCerta Resposta.')
                                print('\nNeighbor é o mesmo que: ')
                                pergunta4 = (
                                    '[1] -> Prima',
                                    '[2] -> Vizinho',
                                    '[3] -> Madrinha',
                                    '[4] -> Namorado',
                                )
                                for loop in pergunta4:
                                    print(loop)

                                select_questao4 = int(input())

                                if select_questao4 == 2:
                                    os.system("cls")
                                    print('\nCerta Resposta.')
                                    print('\nApós o casamento, o que a noiva sera do noivo? ')
                                    pergunta5 = (
                                        '[1] -> Grandmother',
                                        '[2] -> Aunt',
                                        '[3] -> Wife',
                                        '[4] -> Daugther',
                                    )
                                    for loop in pergunta5:
                                        print(loop)

                                    select_questao5 = int(input())

                                    if select_questao5 == 3:
                                        os.system("cls")
                                        print('\nCerta Resposta.')
                                        print('\nQual dos profissionais a seguir trabalha no circo ?')
                                        pergunta6 = (
                                            '[1] -> A doctor',
                                            '[2] -> A clown',
                                            '[3] -> A nurse',
                                            '[4] -> A painter',
                                        )
                                        for loop in pergunta6:
                                            print(loop)

                                        select_questao6 = int(input())

                                        if select_questao6 == 2:
                                            os.system("cls")
                                            print('\nCerta Resposta.')
                                            print('\nQual cor não aparece no arco-íris? ')
                                            pergunta7 = (
                                                '[1] -> Green',
                                                '[2] -> Blue',
                                                '[3] -> Black',
                                                '[4] -> Orange',
                                            )
                                            for loop in pergunta7:
                                                print(loop)

                                            select_questao7 = int(input())

                                            if select_questao7 == 3:
                                                os.system("cls")
                                                print('\nCerta Resposta.')
                                                print('\nSafe is an adjective, what is its related noun?')
                                                pergunta8 = (
                                                    '[1] -> Safety',
                                                    '[2] -> Safely',
                                                    '[3] -> Safeness',
                                                    '[4] -> Safer',
                                                )
                                                for loop in pergunta7:
                                                    print(loop)

                                                select_questao7 = int(input())

                                                if select_questao7 == 1:
                                                    os.system("cls")
                                                    print('\nCerta Resposta.')
                                                    print('\nQual é o significado da palavra inglêsa KING?')
                                                    pergunta9 = (
                                                        '[1] -> Rato',
                                                        '[2] -> Rei',
                                                        '[3] -> Rainha',
                                                        '[4] -> Rã',
                                                    )
                                                    for loop in pergunta9:
                                                        print(loop)

                                                    select_questao9 = int(input())

                                                    if select_questao9 == 2:
                                                        os.system("cls")
                                                        print('\nCerta Resposta.')
                                                        print('\nBoxing day in the uk in on__________________.')
                                                        pergunta10 = (
                                                            '[1] -> December 23',
                                                            '[2] -> December 31',
                                                            '[3] -> December 26',
                                                            '[4] -> December 25',
                                                        )
                                                        for loop in pergunta10:
                                                            print(loop)

                                                        select_questao10 = int(input())

                                                        if select_questao10 == 3:
                                                            os.system("cls")
                                                            print('\nCerta Resposta.')
                                                            print(f'\nPARABENS {nome.upper()} VOCÊ ACERTOU TODAS AS '
                                                                  f'PERGUNTAS')
                                                            input()
                                                        else:
                                                            print('\nResposta Errada!')
                                                            input()
                                                    else:
                                                        print('\nResposta Errada!')
                                                        input()
                                                else:
                                                    print('\nResposta Errada!')
                                                    input()
                                            else:
                                                print('\nResposta Errada!')
                                                input()
                                        else:
                                            print('\nResposta Errada!')
                                            input()
                                    else:
                                        print('\nResposta Errada!')
                                        input()
                                else:
                                    print('\nResposta Errada!')
                                    input()
                            else:
                                print('\nResposta Errada!')
                                input()
                        else:
                            print('\nResposta Errada!')
                            input()
                    else:
                        print('\nResposta Errada!')
                        input()
                else:
                    print('\nResposta Errada!')
                    input()

            elif escolha_materias == 4:
                os.system("cls")
                print(f'\nMuito bem {nome}, vamos ao game!')
                print('\nO que significa lambuzar?')
                pergunta1 = (
                    '[1] -> Sujar',
                    '[2] -> Limpar',
                    '[3] -> Refrescar',
                    '[4] -> Cheirar',
                )
                for loop in pergunta1:
                    print(loop)

                select_questao1 = int(input())

                if select_questao1 == 1:
                    os.system("cls")
                    print('\nCerta Resposta.')
                    print('\nO verbo "TELEFONEAR" em espanhol pode ser substituído por:')
                    pergunta2 = (
                        '[1] -> Chamar',
                        '[2] -> Ligar',
                        '[3] -> LLamar',
                        '[4] -> Conectar',
                    )
                    for loop in pergunta2:
                        print(loop)

                    select_questao2 = int(input())

                    if select_questao2 == 3:
                        os.system("cls")
                        print('\nCerta Resposta.')
                        print('\nComo se diz "cigarro" em espanhol?')
                        pergunta3 = (
                            '[1] -> Cigarro',
                            '[2] -> Puro',
                            '[3] -> Cigarrete',
                            '[4] -> Cigarrillo',
                        )
                        for loop in pergunta3:
                            print(loop)

                        select_questao3 = int(input())

                        if select_questao3 == 4:
                            os.system("cls")
                            print('\nCerta Resposta.')
                            print('\n Ha numa cozinha, em espanhol, exceto: ')
                            pergunta4 = (
                                '[1] -> Plato',
                                '[2] -> Cama',
                                '[3] -> Tenedor',
                                '[4] -> Cuchillo',
                            )
                            for loop in pergunta4:
                                print(loop)

                            select_questao4 = int(input())

                            if select_questao4 == 2:
                                os.system("cls")
                                print('\nCerta Resposta.')
                                print('\nSon platos españoles, expeto: ')
                                pergunta5 = (
                                    '[1] -> Paella',
                                    '[2] -> Gazpacho',
                                    '[3] -> Caruru',
                                    '[4] -> Tortilla de Patatas',
                                )
                                for loop in pergunta5:
                                    print(loop)

                                select_questao5 = int(input())

                                if select_questao5 == 3:
                                    os.system("cls")
                                    print('\nCerta Resposta.')
                                    print('\nEm espanhol, o verbo "QUEDAR" significa:')
                                    pergunta6 = (
                                        '[1] -> Ficar ',
                                        '[2] -> Cair',
                                        '[3] -> Queimar',
                                        '[4] -> Querer',
                                    )
                                    for loop in pergunta6:
                                        print(loop)

                                    select_questao6 = int(input())

                                    if select_questao6 == 1:
                                        os.system("cls")
                                        print('\nCerta Resposta.')
                                        print('\nA expressão "ESTAR EMBARAZADA" em espanhol significa: ')
                                        pergunta7 = (
                                            '[1] -> Estar com medo',
                                            '[2] -> Estar envergonhado',
                                            '[3] -> Estar em apuros',
                                            '[4] -> Estar grávida',
                                        )
                                        for loop in pergunta7:
                                            print(loop)

                                        select_questao7 = int(input())

                                        if select_questao7 == 4:
                                            os.system("cls")
                                            print('\nCerta Resposta.')
                                            print('\nSão meios de transporte, em espanholm exceto:')
                                            pergunta8 = (
                                                '[1] -> Avión',
                                                '[2] -> Tren',
                                                '[3] -> Escorpión',
                                                '[4] -> Bicicleta',
                                            )
                                            for loop in pergunta8:
                                                print(loop)

                                            select_questao8 = int(input)

                                            if select_questao8 == 3:
                                                os.system("cls")
                                                print('\nCerta Resposta.')
                                                print('\n A que parte do corpo se refere a palavra "TOBILLO" em '
                                                      'espanhol: ')
                                                pergunta9 = (
                                                    '[1] -> Tórax',
                                                    '[2] -> Testa',
                                                    '[3] -> Tíbia',
                                                    '[4] -> Tornozelo',
                                                )
                                                for loop in pergunta9:
                                                    print(loop)

                                                select_questao9 = int(input())

                                                if select_questao9 == 4:
                                                    os.system("cls")
                                                    print('\nCerta Resposta.')
                                                    print(
                                                        '\nA expressão "LA COMIDA ESTÁ EXQUISITA" em espanhol '
                                                        'significa:')
                                                    pergunta10 = (
                                                        '[1] -> A comida está estranha',
                                                        '[2] -> A comida está uma delícia',
                                                        '[3] -> A comida está estragada',
                                                        '[4] -> A comida está envenenada',
                                                    )
                                                    for loop in pergunta10:
                                                        print(loop)

                                                    select_questao10 = int(input())

                                                    if select_questao10 == 2:
                                                        os.system("cls")
                                                        print('\nCerta Resposta.')
                                                        print(f'\nPARABENS {nome.upper()} VOCÊ ACERTOU TODAS AS '
                                                              f'PERGUNTAS')
                                                        input()

                                                else:
                                                    print('\nResposta Errada!')
                                                    input()
                                            else:
                                                print('\nResposta Errada!')
                                                input()
                                        else:
                                            print('\nResposta Errada!')
                                            input()
                                    else:
                                        print('\nResposta Errada!')
                                        input()
                                else:
                                    print('\nResposta Errada!')
                                    input()
                            else:
                                print('\nResposta Errada!')
                                input()
                        else:
                            print('\nResposta Errada!')
                            input()
                    else:
                        print('\nResposta Errada!')
                        input()
                else:
                    print('\nResposta Errada!')
                    input()

            elif escolha_materias == 5:
                os.system("cls")
                print(f'\nMuito bem {nome}, vamos ao game!')
                print('\nFesta popular brasileira muito divulgada no exterior: ')
                pergunta1 = (
                    '[1] -> Pascoa',
                    '[2] -> Carnaval',
                    '[3] -> Tourada',
                    '[4] -> Natal',
                )
                for loop in pergunta1:
                    print(loop)

                select_questao1 = int(input())

                if select_questao1 == 2:
                    os.system("cls")
                    print('\nCerta Resposta.')
                    print('\nQual o ano da comemoração dos 500 anos do descobrimento do Brasil?')
                    pergunta2 = (
                        '[1] -> 1998',
                        '[2] -> 1990',
                        '[3] -> 2000',
                        '[4] -> 1997',
                    )
                    for loop in pergunta2:
                        print(loop)

                    select_questao2 = int(input())

                    if select_questao2 == 3:
                        os.system("cls")
                        print('\nCerta Resposta.')
                        print('\nHa quantos anos o Brasil foi descoberto? ')
                        pergunta3 = (
                            '[1] -> 50 anos',
                            '[2] -> 500 anos',
                            '[3] -> 100 anos',
                            '[4] -> 200 anos',
                        )
                        for loop in pergunta3:
                            print(loop)

                        select_questao3 = int(input())

                        if select_questao3 == 2:
                            os.system("cls")
                            print('\nCerta Resposta.')
                            print('\nAquele que ocupa a terra sem ter o título de propriedade chama-se de:')
                            pergunta4 = (
                                '[1] -> Posseiro',
                                '[2] -> Arrendatario',
                                '[3] -> Peão',
                                '[4] -> Bóia-Fria',
                            )
                            for loop in pergunta4:
                                print(loop)

                            select_questao4 = int(input())

                            if select_questao4 == 1:
                                os.system("cls")
                                print('\nCerta Resposta.')
                                print('\nQual é o contrario de altruísmo?')
                                pergunta5 = (
                                    '[1] -> Amor',
                                    '[2] -> Egoísmo',
                                    '[3] -> Ciúme',
                                    '[4] -> Filantropia',
                                )
                                for loop in pergunta5:
                                    print(loop)

                                select_questao5 = int(input())

                                if select_questao5 == 2:
                                    os.system("cls")
                                    print('\nCerta Resposta.')
                                    print('\nQual é o antônimo de ida?')
                                    pergunta6 = (
                                        '[1] -> Retirada',
                                        '[2] -> Fugida',
                                        '[3] -> Volta',
                                        '[4] -> Saída',
                                    )
                                    for loop in pergunta6:
                                        print(loop)

                                    select_questao6 = int(input())

                                    if select_questao6 == 3:
                                        os.system("cls")
                                        print('\nCerta Resposta.')
                                        print('\nQual é o objeto ultilizado pelos deficientes visuais para tatear '
                                              'o caminho?')
                                        pergunta7 = (
                                            '[1] -> Cadeira',
                                            '[2] -> Bengala',
                                            '[3] -> Bengala branca',
                                            '[4] -> Bússola',
                                        )
                                        for loop in pergunta7:
                                            print(loop)

                                        select_questao7 = int(input())

                                        if select_questao7 == 3:
                                            os.system("cls")
                                            print('\nCerta Resposta.')
                                            print('\nDolência significa: ')
                                            pergunta8 = (
                                                '[1] -> Amor',
                                                '[2] -> Magoa',
                                                '[3] -> Alegria',
                                                '[4] -> Paz',
                                            )
                                            for loop in pergunta8:
                                                print(loop)

                                            select_questao8 = int(input())

                                            if select_questao8 == 2:
                                                os.system("cls")
                                                print('\nCerta Resposta.')
                                                print('\nComo é conhecido o colégio que aceita alunos de ambos os '
                                                      'sexo:')
                                                pergunta9 = (
                                                    '[1] -> Mísula',
                                                    '[2] -> Misto',
                                                    '[3] -> Mistol',
                                                    '[4] -> Mítico',
                                                )
                                                for loop in pergunta9:
                                                    print(loop)

                                                select_questao9 = int(input())

                                                if select_questao9 == 2:
                                                    os.system("cls")
                                                    print('\nCerta Resposta.')
                                                    print('\nTermo que define "tudo o que aconte na natureza": ')
                                                    pergunta10 = (
                                                        '[1] -> Acontecimento',
                                                        '[2] -> Precipitção',
                                                        '[3] -> Isolamento',
                                                        '[4] -> Fenômeno',
                                                    )
                                                    for loop in pergunta10:
                                                        print(loop)

                                                    select_questao10 = int(input())

                                                    if select_questao10 == 4:
                                                        os.system("cls")
                                                        print('\nCerta Resposta.')
                                                        print(f'\nPARABENS {nome.upper()} VOCÊ ACERTOU TODAS AS '
                                                              f'PERGUNTAS')
                                                        input()
                                                    else:
                                                        print('\nResposta Errada!')
                                                        input()
                                                else:
                                                    print('\nResposta Errada!')
                                                    input()
                                            else:
                                                print('\nResposta Errada!')
                                                input()
                                        else:
                                            print('\nResposta Errada!')
                                            input()
                                    else:
                                        print('\nResposta Errada!')
                                        input()
                            else:
                                print('\nResposta Errada!')
                                input()
                        else:
                            print('\nResposta Errada!')
                            input()
                    else:
                        print('\nResposta Errada!')
                        input()
                else:
                    print('\nResposta Errada!')
                    input()

            else:
                print('Opção invalida')
                input()

        except ValueError:
            print('Valor Invalido.')
            input()



