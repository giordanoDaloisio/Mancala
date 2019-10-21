__author__ = "giordanodaloisio"

from copy import deepcopy


class MancalaState:

    def __init__(self, board, next_player=None, parent=None):
        self.board = board
        self.parent = parent
        self.next_player = next_player

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

    def print(self):
        print("  ", end="")
        print(*["%2d" % x for x in reversed(self.board[7:13])], sep="|")
        print("%2d                  %2d" % (self.opponent_points, self.player_points))
        print("  ", end="")
        print(*["%2d" % x for x in self.board[0:6]], sep="|")

    def no_moves(self):
        return any(self.board[0:6]) == 0 or any(self.board[7:13]) == 0

    def make_move(self, cell, player):
        # returns a new state corresponding to moving the pots in the <cell> of the <player>

        # check if cell is between 0 and 5 and player is valid one
        if cell in range(0, 6) and player in (0, 7):
            # compute the value of the cell for player 0 or 7
            cell += player
            # check if cell is not empty
            if self.board[cell] > 0:
                new_board = deepcopy(self.board)
                # place pot in adjacent cells
                pos = 0
                for i in range(1, new_board[cell]+1):
                    pos = cell + i
                    if pos > 13:
                        pos = 0
                    new_board[pos] += 1
                new_board[cell] = 0
                # check if player has another turn
                if (player == 1 and pos == 6) or (player == 7 and pos == 13):
                    next_player = player
                else:
                    next_player = 7 - player
                return MancalaState(new_board, next_player, self)


class MancalaGame:

    def __init__(self, board):
        self.state = MancalaState(board)

    def make_move(self, cell, player):
        new_state = self.state.make_move(cell, player)
        self.state = new_state
        return self.state.next_player

    def neighbors(self, player):
        out = set([])
        state = self.state
        for cell in range(0, 6):
            out.add(state.make_move(cell, player))
        return out






