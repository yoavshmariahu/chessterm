"""
chess.py defines the game mechanics of ChessTerm.

Created 7/30/2024
"""

class ChessTerm:
    def __init__(self) -> None:
        # TODO: initialize the chess board to represent any relevant information for the board & pieces.
        self._board = # Fill in.
        # TODO: this variable should store which player's turn it is.
        self._player_to_play = # Fill in.

    def print_board(self) -> None:
        # TODO: create a function that prints out chess board.
        pass

    def move_piece(self, src: str, dest: str) -> None: 
        # TODO: move a piece from a src location to a dest location.
        # TODO: validate that the piece we're attempting to move is the correct color based on is_white.
        pass
