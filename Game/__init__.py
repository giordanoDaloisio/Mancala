from copy import deepcopy

__author__ = "GiordanodAloisio"


class MancalaState:

    # each state is defined by the board, the parent and the points of both the players
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    @property
    def player_points(self):
        if self.no_moves():
            return sum(self.board[7:13])+self.board[6]
        else:
            return self.board[6]

    @property
    def ai_points(self):
        if self.no_moves():
            return sum(self.board[0:6])+self.board[13]
        else:
            return self.board[13]

    def __str__(self):
        ris = "| "
        for cell in self.board:
            ris += str(cell) + " | "
        return ris

    def player_pebbles(self):
        # return the number of pebbles on the player side
        return sum(self.board[0:6])

    def ai_pebbles(self):
        # return the number of pebbles on the ai side
        return sum(self.board[7:13])

    def print(self):
        if not self.no_moves():
            print("  ", end="")
            print(*["%2d" % x for x in reversed(self.board[7:13])], sep="|")
            print("%2d                  %2d" % (self.ai_points, self.player_points))
            print("  ", end="")
            print(*["%2d" % x for x in self.board[0:6]], sep="|")
        else:
            print("  ", end="")
            print(*["%2d" % 0 for x in reversed(self.board[7:13])], sep="|")
            print("%2d                  %2d" % (self.ai_points, self.player_points))
            print("  ", end="")
            print(*["%2d" % 0 for x in self.board[0:6]], sep="|")

    def no_moves(self):
        # check if a player as no more moves
        return self.player_pebbles() == 0 or self.ai_pebbles() == 0

    def neighbors(self, player):
        out = set([])
        for cell in range(0, 6):
            new_state = self.__make_move(cell, player)
            if new_state is not None:
                out.add(new_state)
        return out

    def get_state_info(self):
        return self.board, self.player_points, self.ai_points

    def __make_move(self, cell, player):
        # returns a new state corresponding to moving the pots in the <cell> of the <player>

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
                return MancalaState(new_board, self)


class MancalaGame:

    def __init__(self, board):
        self.state = MancalaState(board)

    def make_move(self, cell, player):
        new_state = self.state.make_move(cell, player)
        self.state = new_state
        return self.state.get_state_info()

    def no_moves(self):
        return self.state.no_moves()

    def winner(self):
        return self.state.player_points > self.state.ai_points

    def draw(self):
        return self.state.player_points == self.state.ai_points

    def set_state(self, state):
        self.state = state
        return self.state.get_state_info()

    def reset(self):
        # reset the board for a new game
        board = [4 for i in range(0, 6)]
        board += [0]
        board += [4 for i in range(0, 6)]
        board += [0]
        self.state = MancalaState(board)
        return self.state.get_state_info()

