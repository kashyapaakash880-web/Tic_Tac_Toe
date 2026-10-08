import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def display():
    print("=" * 35)
    print("          TIC TAC TOE")
    print("=" * 35)
    print(f"You:{player_score}  AI: {ai_score}")
    print()
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

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

def get_available_positions():
    available_positions = []

    for i in range(9):
        if board[i] not in ["X", "O"]:
            available_positions.append(i)

    return available_positions

def random_ai():
    available_positions = get_available_positions()
    random_number = random.randint(0, len(available_positions) - 1)
    return available_positions[random_number]

def ai_move():
    position = random_ai()
    board[position] = "O"
    display()

player_score = 0
ai_score = 0
draw_score = 0

display()

while True:

    player_move("X")

    result = check_win()

    if result:
        print(result)
        if result == "Player X Wins!":
            player_score += 1
            print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        else:
            ai_score += 1
            print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        break

    draw = draw_show()

    if draw:
        print(draw)
        draw_score += 1
        print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        break

    # AI move goes here
    print("AI is thinking...")
    ai_move()

    result_ = check_win()

    if result_:
        print(result_)
        if result_ == "Player X Wins!":
            player_score += 1
            print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        else:
            ai_score += 1
            print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        break

    draw_1 = draw_show()

    if draw_1:
        print(draw_1)
        draw_score += 1
        print(f"\nScore → You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
        break

