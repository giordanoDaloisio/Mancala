__author__ = "giordanodaloisio"


def h1(state, player):
    value = state.ai_points - state.player_points
    # always prefer a move that makes you play again
    # if state.next_player == 7 and player == 7 and not state.no_moves:
    #     value += 100
    return value
