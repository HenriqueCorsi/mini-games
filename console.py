import adivinhe_numero
import pergunta_resposta
import os

print('\n***** SELECIONE O JOGO QUE GOSTARIA DE JOGAR *****')
print('[1] -> Qual é o número\n[2] -> Perguntas e Respostas')
try:
    select_user = int(input())
except ValueError:
    print('Opção Inváida')
else:
    if select_user == 1:
        os.system("cls")
        adivinhe_numero.jogar_advinheNumero()
    elif select_user == 2:
        pergunta_resposta.jogar_perguntaResposta()
    else:
        print('Opção Inváida')


