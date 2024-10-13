


def main():
    while True:
        board = list(range(1, 10))  # Reset the board
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1

            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)



def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

        restart = input("Начать новую игру? (y/n): ")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
    main()

