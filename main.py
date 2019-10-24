from Game import MancalaGame
import Heuristics

MIN = 0
MAX = 7


def minmax(state, player, depth=5):
    beststate = None
    if depth == 0 or state.no_moves():
        return Heuristics.h1(state), state

    if player is MAX:
        currval = float('-inf')
        for node in state.neighbors(MAX):
            val, state = minmax(node, MIN, depth-1)
            if val > currval:
                currval = val
                beststate = node
        return currval, beststate

    if player is MIN:
        currval = float('inf')
        for node in state.neighbors(MIN):
            val, state = minmax(node, MAX, depth-1)
            if val < currval:
                currval = val
                beststate = node
        return currval, beststate


def alpha_beta(state, player, alpha=float('-inf'), beta=float('inf'), depth=10):
    beststate = state
    if state.no_moves() or depth == 0:
        return Heuristics.h1(state), state
    if player is MAX:
        currval = float('-inf')
        for node in state.neighbors(player):
            val, state = alpha_beta(node, MIN, alpha, beta, depth-1)
            alpha = max(alpha, val)
            if val > currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate
    if player is MIN:
        currval = float('inf')
        for node in state.neighbors(player):
            val, state = alpha_beta(node, MAX, alpha, beta, depth-1)
            beta = min(beta, val)
            if val < currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate


def choose_move():
    move = -1
    while move == "" or int(move) not in range(1, 7):
        move = input("Select a cell to pickup [1-6]")
    return int(move)-1


def man_vs_ai(game):
    game.state.print()
    move = choose_move()
    game.make_move(move, MIN)
    player = game.get_next_player()
    while not game.no_moves():
        game.state.print()
        if player is MAX:
            val, move = alpha_beta(game.state, MAX)
            game.set_state(move)
            print("Value: "+str(val))
        elif player is MIN:
            move = choose_move()
            game.make_move(move, player)
        player = game.get_next_player()
    if game.winner():
        print("Hai vinto")
    else:
        print("Hai perso")


def ai_vs_ai(game):
    game.state.print()
    val, move = alpha_beta(game.state, MIN)
    game.state = move
    player = game.get_next_player()
    while not game.no_moves():
        print("Value: " + str(val))
        game.state.print()
        val, move = alpha_beta(game.state, player)
        game.state = move
        player = game.get_next_player()
    if game.winner():
        print("Ha vinto MIN")
    else:
        print("Ha vinto MAX")


board = [4 for i in range(0, 6)]
board += [0]
board += [4 for i in range(0, 6)]
board += [0]
mancala = MancalaGame(board)
man_vs_ai(mancala)
#ai_vs_ai(mancala)