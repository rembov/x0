


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

        restart = input("Начать новую игру? (y/n): ")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
    main()
