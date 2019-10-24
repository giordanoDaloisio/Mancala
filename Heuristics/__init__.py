__author__ = "giordanodaloisio"


class DoubleTurnHeuristic:

    def __init__(self, max, min):
        self.max = max
        self.min = min

    def minmax(self, state, player, depth=5):
        beststate = None
        if depth == 0 or state.no_moves():
            return self.heuristic(state, player), state

        if player is self.max:
            currval = float('-inf')
            for node in state.neighbors(self.max):
                val, state = self.minmax(node, state.next_player, depth - 1)
                if val > currval:
                    currval = val
                    beststate = node
            return currval, beststate

        if player is self.min:
            currval = float('inf')
            for node in state.neighbors(self.min):
                val, state = self.minmax(node, state.next_player, depth - 1)
                if val < currval:
                    currval = val
                    beststate = node
            return currval, beststate

    @classmethod
    def heuristic(cls, state, player):
        value = state.ai_points - state.player_points
        # always prefer a move that makes you play again
        if state.next_player == 7 and player == 7 and not state.no_moves:
            value += 100
        return value


def h1(state):
    # maximize the relative score of the ai
    return state.ai_points - state.player_points