from copy import copy


class MancalaState:

    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    @property
    def player_points(self):
        if self.no_moves():
            return sum(self.board[0:7])
        else:
            return self.board[6]

    @property
    def opponent_points(self):
        if self.no_moves():
            return sum(self.board[7:14])
        else:
            return self.board[13]

    def no_moves(self):
        return any(self.board[0:6]) == 0 or any(self.board[7:13]) == 0

    def make_move(self, cell, player):

        # check if cell is between 0 and 5 and player is valid one
        if cell in range(0,6) and player in [0,7]:

            # check if cell is not empty
            if self.board[cell+player] > 0:
                new_board = copy(self.board)
                pos = cell

                # place pot in adjacent cells
                for i in range(1, new_board[cell]+1):
                    pos += i
                    if pos > 13:
                        pos = 0
                    new_board[pos] += 1

                # check if player has another turn
                if (player == 1 and pos == 6) or (player == 7 and pos == 13):
                    next_player = player
                else:
                    next_player = 7 - player
                return MancalaState(new_board, self), next_player


class MancalaGame:

    def __init__(self, state):
        self.state = state

    def make_move(self, state):
        self.state = state
    






