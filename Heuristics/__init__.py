__author__ = "giordanodaloisio"


def h1(state, player):
    return state.ai_points - state.player_points - abs(player-state.next_player)
