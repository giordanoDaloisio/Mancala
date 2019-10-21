__author__ = "giordanodaloisio"


class Heuristic:

    def __init__(self):
        pass

    def h1(self, state):
        return state.player_points - state.opponent_points
