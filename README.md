# Mini-games

# Introdução

Estou em processo de aprendizagem na linguagem de programação Python e após entrar no tópico de Package, módulos e funções, resolvi criar um arquivo onde estão importados 2 mini game que desenvolvi no decorrer dos meus estudos.
O arquivo principal seria o nomeado como console.py, nele está contido um simples menu onde o usuário escolhera o jogo que gostaria de jogar.
Já os outros dois arquivos (pergunta_resposta.py, adivinhe_numero.py) são a programação em si dos jogos que foram desenvolvidos.
A medida que eu for avançando no meu aprendizado pretendo adicionar mais jogos e até mesmo otimizar os que já estão finalizado, mais para fins de estudo pois meu foco não é desenvolvimento de jogos.

# Techs

Python: Linguagem de programação de sintaxe simples.

# Funcionamento

A imagem abaixo seria o arquivo principal (console.py), nele está contido um menu no qual o usuário irá escolher qual jogo ele gostaria de jogar.


![Console](https://user-images.githubusercontent.com/106001465/171087607-e88906e6-c488-4f2d-9d54-100eb86e2360.PNG)


# Adivinhe o número

O objetivo do usuário é descobrir qual número foi selecionado pelo programa.

Neste primeiro print podemos observar que o modulo random foi importado para o programa poder gerar os números inteiros aleatoriamente,  também é onde o usuário irá escolher a dificuldade que ele gostaria de jogar.

![AN part 1](https://user-images.githubusercontent.com/106001465/171090520-d74d0cd8-4dc2-4144-8dfe-eaff60ba3d4b.PNG)


Já neste segundo print é um exemplo caso seja escolhida a dificuldade fácil. O usuário terá cinco chances de descobrir qual número o programa selecionou de 1 até 10

![an](https://user-images.githubusercontent.com/106001465/171090899-c2c1130b-4ac6-421d-af27-54b91f7adad3.PNG)


Um outro exemplo é caso seja escolhido a dificuldade médio. O usuário terá 10 chances de descobrir qual número o programa selecionou de 1 até 50.

![an](https://user-images.githubusercontent.com/106001465/171091153-dcf86a33-574f-48d4-b3d2-d3f2177ae2a8.PNG)


# Perguntas e Respostas

Este mini game é um programa que eu já continha em um outro repositório, apenas importei para este novo projeto.

Nesse jogo o usuário escolhera dentre as categorias que estarão disponível e respondera perguntas com alternativas relacionadas a categoria que ele escolheu.

Na imagem abaixo é criado um menu de categorias, onde o usuário irá escolher o tema no qual ele gostaria de responder as perguntas. Eu utilizo uma Tuple para armazenar as opções do meu menu e o for loop irá realizar a exibição no formato a qual eu quero para o usuário.

![pr](https://user-images.githubusercontent.com/106001465/171092498-74f7db4f-660c-4772-ab10-375eaea5d044.PNG)

O usuário selecionando o tema matemática por exemplo, será exibido as questões relacionadas a esse tema. Caso ele responda a alternativa correta será direcionado a próxima pergunta, caso responda errado é exibido uma mensagem na tela dizendo que a resposta está errada e o programa será finalizado.

![pr](https://user-images.githubusercontent.com/106001465/171093100-64cb388f-ab80-4cb2-ac7c-d4532ad5c6c6.PNG)


# Jogo da Forca

Os prints abaixo mostra um pouquinho mais da complexidade do código. Resolvi desenvolver esse códigos em partes, cada execução do código está divido em funções, acredito que assim ficar muito melhor para compreender as execuções do programa e possíveis correções e atualizações.

Neste primeiro print está contido as funções que vão coletar os dados do usuário, também temos a função que irá definir a palavra secreta e também a função que irá ser executar caso a palavra informada pelo usuário esteja correta.

![parte01](https://user-images.githubusercontent.com/106001465/171563238-611f3498-48de-4dd1-9167-f09dc2b0ba76.PNG)

Já neste segundo print podemos observar as funções do print acima sendo executas, algumas variáveis importantes sendo declaradas para realizar toda a verificação, para saber se a letra digitada está contida na palavra secreta e todo o processo que é feito caso a letra que o usuário digitar esteja errada.

![parte02](https://user-images.githubusercontent.com/106001465/171564010-94e2b255-6017-4ed9-a8a9-f3124f4ab88f.PNG)



