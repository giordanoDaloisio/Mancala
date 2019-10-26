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
    def h(state, player):
        # maximize the relative score of the player
        if player == 7: # ai side player
            return state.ai_points - state.player_points
        if player == 0: # human side player
            return state.player_points - state.ai_points


class RelativePointsAndPebblesSingleTurnHeuristic:

    @staticmethod
    def h(state, player):
        # maximize the relative score of the player plus the relative number of pebbles on the opponent side
        if player == 7: # ai side player
            return (state.ai_points - state.player_points) * 10 + (state.player_pebbles()-state.ai_pebbles())
        if player == 0: # human side player
            return (state.player_points - state.ai_points) * 10 + (state.ai_pebbles() - state.player_pebbles())


class RightCellSingleTurnHeuristic:

    @staticmethod
    # maximize the relative score plus the amount of pebbles on the right most cell of the his side
    def h(state, player):
        if player == 0:
            return (state.player_points - state.ai_points)*10 + state.board[5]
        if player == 7:
            return (state.ai_points - state.player_points)*10 + state.board[12]