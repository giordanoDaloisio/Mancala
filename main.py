from Game import MancalaGame
from Heuristics import Heuristic

MIN = 0
MAX = 7


def minmax(game, state, player):
    beststate = None

    if state.complete():
        return h.heuristic(state, MAX), state

    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, MAX):
            val, state = minmax(game, node, MIN)
            if val > currval:
                currval = val
                beststate = node

    if player is MIN:
        currval = float('inf')
        for node in game.neighbors(state, MIN):
            val, state = minmax(game, node, MAX)
            if val < currval:
                currval = val
                beststate = node
    return currval, beststate


def alpha_beta(game, state, player, alpha=float('-inf'), beta=float('inf')):
    beststate = state
    if state.complete():
        return h.heuristic(state, MAX), state
    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, player):
            val, state = alpha_beta(game, node, MIN, alpha, beta)
            alpha = max(alpha, val)
            if val > currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate
    if player is MIN:
        currval = float('inf')
        for node in game.neighbors(state, player):
            val, state = alpha_beta(game, node, MAX, alpha, beta)
            beta = min(beta, val)
            if val < currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate