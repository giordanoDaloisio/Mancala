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
    # maximize the relative score plus the amount of pebbles on the right most cell of the his side
    def h(state, player):
        if player == 0:
            return (state.player_points - state.ai_points)*10 + state.board[5]
        if player == 7:
            return (state.ai_points - state.player_points)*10 + state.board[12]