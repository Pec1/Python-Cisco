# Projetos Finais - Curso de Python - Cisco Networking Academy

## Sobre
Este repositório contém os projetos finais desenvolvidos durante o curso de Python da Cisco Networking Academy. Os projetos exploram a manipulação de dados, automação de tarefas e desenvolvimento web.

## Projetos
* **Jogo da Velha:**
   Sua tarefa é escrever um programa simples que finge jogar tic-tac-toe com o usuário. Para tornar tudo mais fácil para você, decidimos simplificar o jogo. Aqui estão nossas suposições:
   
   o computador (ou seja, seu programa) deve jogar usando 'X's;
   o usuário (por exemplo, você) deve jogar usando 'O's;
   o primeiro movimento pertence ao computador - ele sempre coloca seu primeiro 'X' no meio do quadro;
   todos os quadrados são numerados linha por linha, começando com 1 (consulte a sessão de exemplo abaixo para referência)
   o usuário insere seu movimento inserindo o número do quadrado escolhido - o número deve ser válido, ou seja, deve ser um número inteiro, deve ser maior que 0 e menor que 10, e não pode apontar para um campo que já está ocupada;
   o programa verifica se o jogo acabou - há quatro veredictos possíveis: o jogo deve continuar, o jogo termina com um empate, você ganha ou o computador ganha;
   o computador responde seu movimento e a verificação é repetida;
   não implementem qualquer forma de inteligência artificial - uma escolha de campo aleatória feita pelo computador é boa o suficiente para o jogo.
  
  * Requisitos
   Implemente os seguintes recursos:
   
   o painel deve ser armazenado como uma lista de três elementos, enquanto cada elemento é outra lista de três elementos (as listas internas representam linhas) para que todos os quadrados possam ser acessados usando a seguinte sintaxe:
   
   ````board[row][column]````
                     
   cada um dos elementos da lista interna pode conter "O", "X" ou um dígito que representa o número do quadrado (tal quadrado é considerado livre)
   a aparência do quadro deve ser exatamente igual à apresentada no exemplo.
   implementar as funções definidas para você no editor.
   
   O desenho de um número inteiro aleatório pode ser feito utilizando uma função Python chamada randrange(). O programa de exemplo abaixo mostra como usá-lo (o programa imprime dez números aleatórios de 0 a 8).
   
   Observação: a instrução from-import fornece acesso à função randrange definida em um módulo externo do Python chamado de random.
   
   from random import randrange
    
   ```for i in range(10):
    print(randrange(8))```

## Autor
Paulo Victor Lima
pvldotz@gmail.com
