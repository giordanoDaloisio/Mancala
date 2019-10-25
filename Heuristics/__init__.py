__author__ = "giordanodaloisio"


class DoubleTurnHeuristic:

    @staticmethod
    def h(state, player):
        value = state.ai_points - state.player_points
        # always prefer a move that makes you play again
        if state.next_player == 7 and player == 7 and not state.no_moves:
            value += 100
        return value


class RelativePointsSingleTurnHeuristic:

    @staticmethod
    def h(state):
        # maximize the relative score of the ai
        return state.ai_points - state.player_points


class RelativePointsAndPebblesSingleTurnHeuristic:

    @staticmethod
    def h(state):
        # maximize the relative score of the ai plus the number of pebbles on the opponent side
        return (state.ai_points - state.player_points)*10 + (state.player_pebbles()-state.ai_pebbles())
