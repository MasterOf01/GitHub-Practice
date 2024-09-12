def print_board(board):
    # Prints the current state of the board
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw(board):
    # Check if the board is full and there is no winner
    return all([cell != " " for row in board for cell in row])


def get_move(player):
    # Get a valid move from the player
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter 0, 1, or 2 for both row and column.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def main():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken. Choose another cell.")
            continue

        # Check for a win or a draw
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()