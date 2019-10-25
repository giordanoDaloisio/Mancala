from Game import MancalaGame
import Heuristics as h

MIN = 0
MAX = 7

DOUBLE_TURN_H = h.DoubleTurnHeuristic()
SINGLE_TURN_H = h.RelativePointsSingleTurnHeuristic()
SINGLE_TURN_PEBBLES_H = h.RelativePointsAndPebblesSingleTurnHeuristic()


class DoubleTurn:

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def minmax(self, state, player, depth=5):
        beststate = None
        if depth == 0 or state.no_moves():
            return self.heuristic.h(state, player), state

        if player is MAX:
            currval = float('-inf')
            for node in state.neighbors(MAX):
                val, state = self.minmax(node, state.next_player, depth - 1)
                if val > currval:
                    currval = val
                    beststate = node
            return currval, beststate

        if player is MIN:
            currval = float('inf')
            for node in state.neighbors(MIN):
                val, state = self.minmax(node, state.next_player, depth - 1)
                if val < currval:
                    currval = val
                    beststate = node
            return currval, beststate

    def man_vs_ai(self, game):
        game.state.print()
        move = choose_move()
        game.make_move(move, MIN)
        player = game.get_next_player()
        while not game.no_moves():
            game.state.print()
            if player is MAX:
                val, move = self.minmax(game.state, player)
                game.set_state(move)
                print("Value: "+str(val))
            elif player is MIN:
                move = choose_move()
                game.make_move(move, player)
            player = game.get_next_player()
        game.state.print()
        if game.winner():
            print("Hai vinto")
        elif game.draw():
            print("Pareggio")
        else:
            print("Hai perso")

    def ai_vs_ai(self, game):
        game.state.print()
        val, move = self.minmax(game.state, MIN)
        game.state = move
        player = game.get_next_player()
        while not game.no_moves():
            print("Value: " + str(val))
            game.state.print()
            val, move = self.minmax(game.state, player)
            game.state = move
            player = game.get_next_player()
        game.state.print()
        if game.winner():
            print("Ha vinto MIN")
        elif game.draw():
            print("Pareggio")
        else:
            print("Ha vinto MAX")


class SingleTurn:

    @staticmethod
    def minmax(state, player, heuristic, depth=10):
        beststate = None
        if depth == 0 or state.no_moves():
            return heuristic.h(state), state

        if player is MAX:
            currval = float('-inf')
            for node in state.neighbors(MAX):
                val, state = SingleTurn.minmax(node, MIN, heuristic, depth - 1)
                if val > currval:
                    currval = val
                    beststate = node
            return currval, beststate

        if player is MIN:
            currval = float('inf')
            for node in state.neighbors(MIN):
                val, state = SingleTurn.minmax(node, MAX, heuristic, depth - 1)
                if val < currval:
                    currval = val
                    beststate = node
            return currval, beststate

    @staticmethod
    def alpha_beta(state, player, heuristic, alpha=float('-inf'), beta=float('inf'), depth=15):
        beststate = state
        if state.no_moves() or depth == 0:
            return heuristic.h(state), state
        if player is MAX:
            currval = float('-inf')
            for node in state.neighbors(player):
                val, state = SingleTurn.alpha_beta(node, MIN, heuristic, alpha, beta, depth - 1)
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
                val, state = SingleTurn.alpha_beta(node, MAX, heuristic, alpha, beta, depth - 1)
                beta = min(beta, val)
                if val < currval:
                    currval = val
                    beststate = node
                if alpha >= beta:
                    break
            return currval, beststate

    def man_vs_ai(self, game, heuristic, depth):
        game.state.print()
        move = choose_move()
        game.make_move(move, MIN)
        player = MAX
        while not game.no_moves():
            game.state.print()
            if player is MAX:
                val, move = self.alpha_beta(game.state, player, heuristic, depth=depth)
                game.set_state(move)
                print("Value: "+str(val))
                player = MIN
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

    def ai_vs_ai(self, game, heuristic_max, heuristic_min, max_depth, min_depth):
        game.state.print()
        val, move = self.alpha_beta(game.state, MIN, heuristic_min, depth=min_depth)
        game.state = move
        player = MAX
        while not game.no_moves():
            print("Value: " + str(val))
            game.state.print()
            if player is MAX:
                val, move = self.alpha_beta(game.state, player, heuristic_max, depth=max_depth)
            elif player is MIN:
                val, move = self.alpha_beta(game.state, player, heuristic_min, depth=min_depth)
            game.state = move
            if player is MAX:
                player = MIN
            elif player is MIN:
                player = MAX
        game.state.print()
        if game.winner():
            print("Ha vinto MIN")
        elif game.draw():
            print("Pareggio")
        else:
            print("Ha vinto MAX")


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


board = [4 for i in range(0, 6)]
board += [0]
board += [4 for i in range(0, 6)]
board += [0]
mancala = MancalaGame(board)
double_turn_game = DoubleTurn(DOUBLE_TURN_H)
single_turn_game = SingleTurn()
#single_turn_game.man_vs_ai(mancala, 6)
single_turn_game.ai_vs_ai(mancala, SINGLE_TURN_H, SINGLE_TURN_PEBBLES_H, 10, 10)
#double_turn_game.man_vs_ai(mancala)


