import adivinhe_numero
import pergunta_resposta

print('\n**** SELECIONE O JOGO QUE GOSTARIA DE JOGAR ****')
print('[1] -> Qual é o número\n[2] -> Perguntas e Respostas')

select_user = int(input())

if select_user == 1:
    adivinhe_numero.jogar_advinheNumero()
elif select_user == 2:
    pergunta_resposta.jogar_perguntaResposta()

