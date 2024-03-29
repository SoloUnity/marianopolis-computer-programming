"""
Gordon Ng , 2031408
420-LCU Computer Programming , Monday , November 15
R. Vincent , instructor Assignment 3, Exercise 2 and 3
"""
'''Implements the logic for the game Reversi, based on the "Othello"
version trademarked by Mattel.'''

from board import *

HUMAN = 1
COMPUTER = 2

# DO NOT MODIFY THIS FUNCTION
def game_start():
    '''Create and initialize the game data.

    Returns a properly initialized board object.
    '''
    # Create a board object.
    board = board_create()
    # Set up the initial board configuration for Reversi.
    board_put(board, 3, 3, COMPUTER)
    board_put(board, 4, 4, COMPUTER)
    board_put(board, 3, 4, HUMAN)
    board_put(board, 4, 3, HUMAN)
    # Return the newly-created board object.
    return board

# DO NOT MODIFY THIS FUNCTION
def game_turn(board, row, col):
    '''
    board (list): an object returned by board_create()
    row (int): The row coordinate where the piece should be placed.
    col (int): The column coordinate where the piece should be placed.

    Place the human player's piece on the board at the coordinates 
    row, col.

    If the move is not legal, this function will return False.

    If the move is legal, this function will 'flip over' all of the opponent's
    pieces affected by this move.

    It will then allow the computer player to choose and perform a move, 
    turning over all of the human player's affected pieces.
    '''
    if _is_legal_move(board, row, col, HUMAN):
        # Perform the human player's chosen move.
        board_put(board, row, col, HUMAN)
        _do_flips(board, row, col, HUMAN)
        while True:
            moves = _get_legal_moves(board, COMPUTER)
            if len(moves) > 0:
                row, col = _choose_move(board, moves, COMPUTER)
                # If _choose_move() returns an illegal move, we
                # will catch that here.
                assert _is_legal_move(board, row, col, COMPUTER)
                board_put(board, row, col, COMPUTER)
                _do_flips(board, row, col, COMPUTER)
            else:
                break
            # See if the human has any legal moves left.
            moves = _get_legal_moves(board, HUMAN)
            if len(moves) > 0:
                break
        return True
    else:
        return False

# PUT YOUR game_over() FUNCTION AFTER THIS LINE.
def game_over(board):
    """
    board (list): an object returned by board_create()

    Checks if the human and the computer have any legal moves

    Returns True if they dont have any legal moves
    """
    if len(_get_legal_moves(board, HUMAN)) == 0 and len(_get_legal_moves(board, COMPUTER)) == 0:    #Checks if there are any remaining legal moves
        return True

# PUT YOUR game_winner() FUNCTION AFTER THIS LINE.
def game_winner(board):
    """
    board (list): an object returned by board_create()

    Compares the number of placed human owned pieces versus computer owned pieces

    Returns the player with more pieces or 0 for a tie
    """
    if board_count(board, HUMAN) > board_count(board,COMPUTER): #Compares human score vs computer score
        return HUMAN
    elif board_count(board,COMPUTER) > board_count(board, HUMAN): #Compares computer score vs human score
        return COMPUTER
    else:
        return 0

#
# All of the functions after this point are "private" functions not
# intended to be used outside this module.
#
# That is why their names start with a single underscore.
#

# DO NOT MODIFY THIS FUNCTION
def _get_opponent(player):
    '''
    player (int): HUMAN or COMPUTER
    
    Returns the opponent of the given player.
    '''
    if player == HUMAN:
        return COMPUTER
    else:
        return HUMAN

# DO NOT MODIFY THIS FUNCTION
def _get_flips(board, r0, c0, player, opponent):
    '''
    board (list): an object returned from board_create()
    r0 (int): row number of the proposed move.
    c0 (int): column number of the proposed move.
    player (int): HUMAN or COMPUTER
    opponent (int): COMPUTER or HUMAN
    
    Returns a list of tuples (row, column) that would change color if the 
    player moves to position r0,c0. The length of this list will tell you
    how many pieces would flip for this move.

    The algorithm here just starts at the r0,c0 position and searches
    along each of the eight directions for possible pieces to flip.
    '''
    # Reflects the 8 directions relative to a board position.
    deltas = (( 1, 0), (-1, 0), ( 0, 1), ( 0,-1),
              (-1,-1), ( 1, 1), (-1, 1), ( 1,-1))
    result = []
    n_rows = board_rows(board)
    n_cols = board_cols(board)
    for dr, dc in deltas:
        row = r0 + dr
        col = c0 + dc
        # Start assembling possible flips
        possible = []
        while 0 <= row < n_rows and 0 <= col < n_cols:
            if board_get(board, row, col) == opponent:
                possible += [(row, col)]
            elif board_get(board, row, col) == player:
                # If we found one of our anchor pieces, everything
                # up to this position will flip, so this should
                # be saved in the result list.
                result += possible
                break
            else:
                # No anchor piece found, so we won't flip anything
                # along this direction.
                break
            row += dr
            col += dc

    return result

# DO NOT MODIFY THIS FUNCTION
def _is_legal_move(board, row, col, player):
    '''
    board (list): an object created by board_create()
    row (int): the row coordinate of the proposed move.
    col (int): the column coordinate of the proposed move.
    player (int): HUMAN or COMPUTER

    Return True if a given move is legal.
    '''
    if board_get(board, row, col): # Square is occupied.
        return False
    opponent = _get_opponent(player)
    flips = _get_flips(board, row, col, player, opponent)
    return len(flips) != 0      # A move must flip at least one piece.

# DO NOT MODIFY THIS FUNCTION
def _do_flips(board, row, col, player):
    '''
    board (list): an object created by board_create()
    row (int): the row coordinate of the proposed move.
    col (int): the column coordinate of the proposed move.
    player (int): HUMAN or COMPUTER

    Flip all of the appropriate pieces in response to a move.

    Returns None
    '''
    opponent = _get_opponent(player)
    for rp, cp in _get_flips(board, row, col, player, opponent):
        board_put(board, rp, cp, player)
    
# DO NOT MODIFY THIS FUNCTION
def _get_legal_moves(board, player):
    '''
    board (list): an object created by board_create()
    player (int): HUMAN or COMPUTER

    Return a list containing all of the possible legal moves for this 
    player. A move is represented as a tuple of integers of the form
    (row, col).'''
    result = []
    for row in range(board_rows(board)):
        for col in range(board_cols(board)):
            if _is_legal_move(board, row, col, player):
                result += [(row, col)]
    return result

# PUT YOUR _choose_move() FUNCTION AFTER THIS LINE.
def _choose_move(board, moves, player):
    """
    board (list): an object created by board_create()
    moves (tuple): a tuple list of legal moves obtained from _is_legal_move() and created from def _get_legal_moves()
    player (int): HUMAN or COMPUTER

    Returns and chooses a move from the tuple moves based on the highest obtained score
    """
    tempList = []
    counter = 0
    for move in moves:      #Goes through each legal move
        if len(_get_flips(board, move[0], move[1], player, _get_opponent(player))) > counter:   #Determines if that legal move returns a higher score (flipped pieces) than the one stored by tempList and counter
            tempList.append(move)                                                               #Adds a legal move to the end if it is higher than the one stored
            counter = len(_get_flips(board, move[0], move[1], player, _get_opponent(player)))
    return tempList[-1]




# TESTING CODE. DO NOT CHANGE ANYTHING AFTER THIS LINE!!
# When running standalone, run a few tests of the provided functions.

if __name__ == "__main__":
    print("Testing the game logic.")
    from random import randint
    # Play ten randomized games and make sure nothing breaks.
    for trial in range(10):
        board = game_start()
        moves = _get_legal_moves(board, HUMAN)
        assert len(moves) == 4
        assert (2, 3) in moves
        assert (3, 2) in moves
        assert (4, 5) in moves
        assert (5, 4) in moves

        assert not game_over(board)

        assert game_turn(board, 3, 2)

        # Now play a game automatically.
        n_turns = 1
        while not game_over(board):
            moves = _get_legal_moves(board, HUMAN)
            if len(moves) > 0:
                assert all(_is_legal_move(board, r, c, HUMAN) for r, c in moves)
                # Select move at random.
                move = moves[randint(0, len(moves) - 1)]
                assert game_turn(board, *move)
            assert n_turns < 64 # avoid possible infinite loop
            n_turns += 1

        if game_over(board):
            assert (not _get_legal_moves(board, HUMAN) and
                    not _get_legal_moves(board, COMPUTER))
            
        n_h = board_count(board, HUMAN)
        n_c = board_count(board, COMPUTER)
        print("Trial game ends with:", n_h, n_c)
        if n_h > n_c:
            assert game_winner(board) == HUMAN
        elif n_h < n_c:
            assert game_winner(board) == COMPUTER
        else:
            assert game_winner(board) == 0

    print("All tests passed.")
