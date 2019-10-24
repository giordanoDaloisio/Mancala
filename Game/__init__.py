from copy import deepcopy

__author__ = "giordanodaloisio"


class MancalaState:

    # each state is defined by the board, the parent, the player playing next and the points of both the players
    def __init__(self, board, next_player=None, parent=None):
        self.board = board
        self.parent = parent
        self.next_player = next_player

    def __str__(self):
        ris = "| "
        for cell in self.board:
            ris += str(cell) + " | "
        return ris

    @property
    def player_points(self):
        if self.no_moves():
            return sum(self.board[7:14])
        else:
            return self.board[6]

    @property
    def ai_points(self):
        if self.no_moves():
            return sum(self.board[0:7])
        else:
            return self.board[13]

    def print(self):
        print("  ", end="")
        print(*["%2d" % x for x in reversed(self.board[7:13])], sep="|")
        print("%2d                  %2d" % (self.ai_points, self.player_points))
        print("  ", end="")
        print(*["%2d" % x for x in self.board[0:6]], sep="|")

    def no_moves(self):
        # check if a player as no more moves
        return any(self.board[0:6]) == 0 or any(self.board[7:13]) == 0

    def make_move(self, cell, player):  # returns a new state corresponding to moving the pots in the <cell> of the
        # <player>
        # check if cell is between 0 and 5 and player is valid one
        if cell in range(0, 6) and player in (0, 7):
            # compute the value of the cell for player 0 or 7
            cell += player
            # check if cell is not empty
            if self.board[cell] > 0:
                new_board = deepcopy(self.board)
                # place pot in adjacent cells
                tokens = new_board[cell]
                new_board[cell] = 0
                while tokens > 0:
                    cell += 1
                    if cell > 13:
                        cell = 0
                    new_board[cell] += 1
                    tokens -= 1
                # check if player has another turn
                if (player == 0 and cell == 6) or (player == 7 and cell == 13):
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

    def neighbors(self, state, player):
        out = set([])
        for cell in range(0, 6):
            new_state = state.make_move(cell, player)
            if new_state is not None:
                out.add(new_state)
        return out

    def no_moves(self):
        return self.state.no_moves()

    def winner(self):
        return self.state.player_points > self.state.ai_points

    def get_next_player(self):
        # return the value of the next player
        return self.state.next_player
