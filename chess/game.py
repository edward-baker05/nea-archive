'''The module that handles the calling of most of the game setup and logic'''

def process(coordinate: str) -> tuple:
    '''Convert board coordinates into array index'''
    return (int(coordinate[1]) - 1, ord(coordinate[0]) - 97)

def reset_turn(board) -> None:
    '''Used to reset the turn if the user enters an invalid move'''
    board.print_board()
    turn(board)

def turn(board) -> bool:
    '''Makes the turn'''
    start = get_move(True, board)
    end = get_move(False, board)
    # try:

    # except:
    #     reset_turn(board)

    board.move(start, end)
    return board.is_won()

def get_move(start, board) -> tuple:
    '''Gets the move from the user'''
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    order = 'target' if start else 'destination'

    location = input(f"Enter the location of the {order} square: ")

    if location[0] in valid_letters:
        location = process(location)
    else:
        reset_turn(board)

    return location

def main():
    '''Main function'''
    # Wiping log file when game ran for the first time
    open('log.log', 'w', encoding="utf-8").close()

    board = Board()

    board.load_from_fen()
    won = False

    while not won:
        # board.debugPrint()
        board.print_board()
        won = turn(board)

if __name__ == '__main__':
    from board import Board
    main()
else:
    print("File run incorrectly - Please run game.py directly")

 # TODO Move validation doesn't work for pawns, maybe other pieces too