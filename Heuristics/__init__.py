__author__ = "giordanodaloisio"


def h1(state):
    # maximize the relative score of the ai
    return state.ai_points - state.player_points
