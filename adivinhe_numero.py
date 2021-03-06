from random import randint
import os


def jogar_advinheNumero():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print('\nEm qual nível de dificuldade gostaria de jogar? ')
    print('1 -> Fácil \n2 -> Médio \n3 -> Díficil')
    try:
        dificuldade = int(input())
    except ValueError:
        print('Opção Inválida')
    else:
        try:
            if dificuldade == 1:
                numero_secreto = randint(1, 10)
                os.system("cls")
                for loop in range(5, -1, -1):
                    num = int(input('\nDigite um número entre 1 a 10: '))

                    if num < 1 or num > 10:
                        print('\nVocê deve digitar um número entre 1 a 10')
                        print(f'Você tem apenas {loop} de tentativas')
                        loop = loop - 1
                        continue

                    if num == numero_secreto:
                        print('\nParábens. Você acertou o número secreto!')
                        input()
                        break

                    else:
                        print('\nVocê errou!')

                        if num > numero_secreto:
                            print('Seu palpite foi MAIOR que o número secreto')

                        elif num < numero_secreto:
                            print('Seu palpite foi MENOR que o número secreto')

                        print(f'\nVocê tem apenas {loop} de tentativas')

                        loop = loop - 1

                print(f'O número secreto era: {numero_secreto}')
                input()

            elif dificuldade == 2:
                numero_secreto = randint(1, 50)
                os.system("cls")
                for loop in range(9, -1, -1):

                    num = int(input('\nDigite um número entre 1 a 50: '))

                    if num < 1 or num > 50:
                        print('\nVocê deve digitar um número entre 1 a 50')
                        print(f'Você tem apenas {loop} de tentativas')
                        loop = loop - 1
                        continue

                    if num == numero_secreto:
                        print('\nParábens. Você acertou o número secreto!')
                        input()
                        break

                    else:
                        print('\nVocê errou!')

                        if num > numero_secreto:
                            print('Seu palpite foi MAIOR que o número secreto')

                        elif num < numero_secreto:
                            print('Seu palpite foi MENOR que o número secreto')

                        print(f'\nVocê tem apenas {loop} de tentativas')

                        loop = loop - 1

                print(f'O número secreto era: {numero_secreto}')
                input()

            elif dificuldade == 3:
                numero_secreto = randint(1, 100)
                os.system("cls")
                for loop in range(14, -1, -1):

                    num = int(input('\nDigite um número entre 1 a 100: '))

                    if num < 1 or num > 100:
                        print('\nVocê deve digitar um número entre 1 a 100')
                        print(f'Você tem apenas {loop} de tentativas')
                        loop = loop - 1
                        continue

                    if num == numero_secreto:
                        print('\nParábens. Você acertou o número secreto!')
                        input()
                        break

                    else:
                        print('\nVocê errou!')

                        if num > numero_secreto:
                            print('Seu palpite foi MAIOR que o número secreto')

                        elif num < numero_secreto:
                            print('Seu palpite foi MENOR que o número secreto')

                        print(f'\nVocê tem apenas {loop} de tentativas')

                        loop = loop - 1

                print(f'O número secreto era: {numero_secreto}')
                input()

            else:
                print('Opção Inválida')
                input()

        except ValueError:
            print('Opção Inválida')
            input()
