from Game import MancalaGame
import Heuristics

MIN = 0
MAX = 7


def minmax(game, state, player, depth=10):
    beststate = None

    if depth == 0 or state.no_moves():
        return Heuristics.h1(state), state

    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, MAX):
            val, state = minmax(game, node, MIN, depth-1)
            if val > currval:
                currval = val
                beststate = node
        return currval, beststate

    if player is MIN:
        currval = float('inf')
        for node in game.neighbors(state, MIN):
            val, state = minmax(game, node, MAX, depth-1)
            if val < currval:
                currval = val
                beststate = node
        return currval, beststate


def alpha_beta(game, state, player, alpha=float('-inf'), beta=float('inf'), depth=10):
    beststate = state
    if state.no_moves() or depth == 0:
        return Heuristics.h1(state), state
    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, player):
            val, state = alpha_beta(game, node, MIN, alpha, beta, depth-1)
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
            val, state = alpha_beta(game, node, MAX, alpha, beta, depth-1)
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
    player = MAX
    while not game.no_moves():
        game.state.print()
        if player is MAX:
            val, move = alpha_beta(game, game.state, MAX)
            game.state = move
            player = MIN
            print("Value: "+str(val))
        elif player is MIN:
            move = choose_move()
            game.make_move(move, player)
            player = MAX
    game.state.print()
    if game.winner():
        print("Hai vinto")
    elif game.draw():
        print("Pareggio")
    else:
        print("Hai perso")


def ai_vs_ai(game):
    game.state.print()
    val, move = alpha_beta(game, game.state, MIN)
    game.state = move
    player = MAX
    while not game.no_moves():
        print("Value: " + str(val))
        game.state.print()
        val, move = alpha_beta(game, game.state, player)
        game.state = move
        if player is MAX:
            player = MIN
        elif player is MIN:
            player = MAX
    game.state.print()
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
