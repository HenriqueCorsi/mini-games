def bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")


def variavel_palavra_secreta():
    palavra_secreta = 'python'
    return palavra_secreta


def armazena_letras(palavra):
    return ['_' for letra in palavra]


def entrada_usuario():
    palpite = str(input('\nDigite uma letra: '))
    palpite = palpite.strip()
    return palpite


def palpite_correto(palpite, letras_armazenadas, palavra_secreta, index):
    for letra in palavra_secreta:
        if palpite.lower() == letra:
            letras_armazenadas[index] = letra
        index = index + 1


def print_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_perdeu(palavra_secreta):
    print(f'\nVocê não tem mais chances. A a palavra secreta era: {palavra_secreta}')
    print("    _______________")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if (chances == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (chances == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (chances == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (chances == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (chances == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (chances == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chances == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def forca():
    bem_vindo()  # Função
    palavra_secreta = variavel_palavra_secreta()  # Função
    letras_armazenadas = armazena_letras(palavra_secreta)  # Função
    print(letras_armazenadas)

    errou = False
    acertou = False
    chances = 8
    index = 0

    while not errou and not acertou:
        palpite = entrada_usuario()  # Função

        if palpite in palavra_secreta:
            palpite_correto(palpite, letras_armazenadas, palavra_secreta, index)  # Função
        else:
            chances = chances - 1
            print(f'A letra {palpite} não está contida na palavra-secreta')
            print(f'\nVocê tem {chances} chances!!')
            desenha_forca(chances)  # Função

        errou = chances == 0
        acertou = '_' not in letras_armazenadas
        print(letras_armazenadas)

    if acertou:
        print_ganhou()  # Função
    else:
        print_perdeu(palavra_secreta)  # Função
