__author__ = "giordanodaloisio"


class RelativePointsHeuristic:

    @staticmethod
    def h(state, player):
        # maximize the relative score of the player
        if player == 7:  # ai side player
            return state.ai_points - state.player_points
        if player == 0:  # human side player
            return state.player_points - state.ai_points


class PebblesHeuristic:

    @staticmethod
    def h(state, player):
        # maximize the relative score of the player plus the relative number of pebbles on the opponent side
        if player == 7:  # ai side player
            return (state.ai_points - state.player_points) * 10 + (state.player_pebbles()-state.ai_pebbles())
        if player == 0:  # human side player
            return (state.player_points - state.ai_points) * 10 + (state.ai_pebbles() - state.player_pebbles())


class RightCellHeuristic:

    @staticmethod
    def h(state, player):
        # maximize the relative score plus the amount of pebbles on the right most cell of the his side
        if player == 0:
            return (state.player_points - state.ai_points) * 10 + state.board[5]
        if player == 7:
            return (state.ai_points - state.player_points) * 10 + state.board[12]


class LinearCombinationHeuristic:

    def __init__(self, coeff):
        self.coeff = coeff

    def h(self, state, player):
        point1 = self.coeff[0] * RelativePointsHeuristic.h(state, player)
        point2 = self.coeff[1] * PebblesHeuristic.h(state, player)
        point3 = self.coeff[2] * RightCellHeuristic.h(state, player)
        return (point1+point2+point3)/sum(self.coeff)
