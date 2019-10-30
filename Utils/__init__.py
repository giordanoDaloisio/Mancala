
def minmax(state, player, heuristic, min_player, max_player, depth=10):
    beststate = None
    if depth == 0 or state.no_moves():
        return heuristic.h(state), state

    if player is max_player:
        currval = float('-inf')
        for node in state.neighbors(max_player):
            val, state = minmax(node, min_player, heuristic, depth - 1)
            if val > currval:
                currval = val
                beststate = node
        return currval, beststate

    if player is min_player:
        currval = float('inf')
        for node in state.neighbors(min_player):
            val, state = minmax(node, max_player, heuristic, depth - 1)
            if val < currval:
                currval = val
                beststate = node
        return currval, beststate


def alpha_beta(state, player, heuristic, max_player, min_player, alpha=float('-inf'), beta=float('inf'), depth=15):
    beststate = state
    if state.no_moves() or depth == 0:
        return heuristic.h(state, max_player), state

    if player is max_player:
        currval = float('-inf')
        for node in state.neighbors(player):
            val, state = alpha_beta(
                node, min_player, heuristic, max_player, min_player, alpha, beta, depth - 1)
            alpha = max(alpha, val)
            if val > currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate

    if player is min_player:
        currval = float('inf')
        for node in state.neighbors(player):
            val, state = alpha_beta(
                node, max_player, heuristic, max_player, min_player, alpha, beta, depth - 1)
            beta = min(beta, val)
            if val < currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate


def choose_move():
    input_column = input("Pick up a cell [1-6]: ")
    retrying = False
    while True:
        if retrying:
            input_column = input("Cell not valid try again: ")
        try:
            selected_column = int(input_column)
            if 0 < selected_column < 7:
                return selected_column - 1
            else:
                retrying = True
        except ValueError:
            retrying = True
