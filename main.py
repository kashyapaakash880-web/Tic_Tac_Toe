board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def check_win():
    for combination in winning_combinations:

        col = (
            board[combination[0]],
            board[combination[1]],
            board[combination[2]]
        )

        if all(value_x=="X" for value_x in col):
            return "Player X Wins!"


        elif all(value_o=="O" for value_o in col):
            return "Player O Wins!"


    return None

def draw_show():
    if all(value=="X" or value=="O" for value in board):
        return "It's a Draw!"
    return None

def player_move(player):
    while True:
        position = input(f"Player {player} Choose a position (1-9): ")
        position = int(position)

        if board[position - 1] == str(position):
            board[position - 1] = player
            display()
            break

        else:
            print("Position already taken. Please choose another position!")

player_score = 0
player_score_2 = 0
draw_score = 0

def display():
    print("=" * 35)
    print("          TIC TAC TOE")
    print("=" * 35)
    print(f" Player 1 :{player_score}  Player 2 : {player_score_2}")
    print()
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


display()

while True:

    player_move("X")

    result = check_win()

    if result:
        print(result)
        if result == "Player X Wins!":
            player_score += 1
            print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")
        else:
            player_score_2 += 1
            print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")
        break

    draw = draw_show()
    if draw:
        print(draw)
        draw_score += 1
        print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")
        break

    player_move("O")

    result_ = check_win()

    if result_:
        print(result_)
        if result_ == "Player O Wins!":
            player_score_2 += 1
            print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")

        else:
            player_score += 1
            print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")
        break

    draw_1 = draw_show()
    if draw_1:
        print(draw_1)
        draw_score += 1
        print(f"\nScore → You: {player_score} | AI: {player_score_2} | Draws: {draw_score}")
        break




