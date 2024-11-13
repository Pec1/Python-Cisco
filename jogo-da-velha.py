from random import randrange

def display_board(board):
    # A função aceita um parâmetro contendo o status atual da placa
    # e o imprime no console.
    print("+-----+-----+-----+")
    for row in board:
        print("|", " | ".join(str(x).center(3) for x in row), "|")
        print("+-----+-----+-----+")

def enter_move(board):
    # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
    # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    while True:
        try:
            move = int(input("Digite seu movimento (1-9): "))
            if move < 1 or move > 9:
                print("Por favor, insira um número entre 1 e 9.")
            else:
                row, col = divmod(move - 1, 3)
                if board[row][col] == 'O' or board[row][col] == 'X':
                    print("Esse campo já está ocupado. Tente novamente.")
                else:
                    board[row][col] = 'O'
                    break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 9.")

def make_list_of_free_fields(board):
    # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
    # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # A função analisa o estado da placa a fim de verificar se 
    # o jogador usando 'O's ou 'X's ganhou o jogo
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # A função desenha o movimento do computador e atualiza o tabuleiro.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def display_turn(turn):
    # Exibe quem é a vez de jogar
    if turn == 'O':
        print("É a sua vez (O)!")
    else:
        print("É a vez do computador (X)!")

def main():
    # Inicializando o tabuleiro vazio
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Definindo o jogador e o computador
    player = 'O'
    computer = 'X'
    
    # O computador começa colocando um 'X' no meio
    board[1][1] = 'X'
    display_board(board)
    display_turn('X')  # O computador começa

    turn = player  # A vez do jogador começa após o computador

    while True:
        # Exibe quem é a vez de jogar
        display_turn(turn)
        
        if turn == player:
            # A vez do jogador (usuário)
            enter_move(board)
            display_board(board)

            # Verificar se o jogador ganhou
            if victory_for(board, 'O'):
                print("Você ganhou!")
                break

            # Verificar se o jogo terminou em empate
            if not make_list_of_free_fields(board):
                print("Empate!")
                break

            # Muda a vez para o computador
            turn = computer

        else:
            # A vez do computador
            draw_move(board)
            display_board(board)

            # Verificar se o computador ganhou
            if victory_for(board, 'X'):
                print("O computador ganhou!")
                break

            # Verificar se o jogo terminou em empate
            if not make_list_of_free_fields(board):
                print("Empate!")
                break

            # Muda a vez para o jogador
            turn = player

if __name__ == "__main__":
    main()
