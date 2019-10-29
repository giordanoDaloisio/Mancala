from Game import MancalaGame
import Heuristics as h
from time import time

MIN = 0
MAX = 7

DOUBLE_TURN_H = h.DoubleTurnHeuristic()
SINGLE_TURN_H = h.RelativePointsSingleTurnHeuristic()
SINGLE_TURN_PEBBLES_H = h.RelativePointsAndPebblesSingleTurnHeuristic()
SINGLE_TURN_RIGHT_H = h.RightCellSingleTurnHeuristic()

# class DoubleTurn:
#
#     def minmax(self, state, player, heuristic, depth=5):
#         beststate = None
#         if depth == 0 or state.no_moves():
#             return heuristic.h(state, player), state
#
#         if player is MAX:
#             currval = float('-inf')
#             for node in state.neighbors(MAX):
#                 val, state = self.minmax(node, state.next_player, depth - 1)
#                 if val > currval:
#                     currval = val
#                     beststate = node
#             return currval, beststate
#
#         if player is MIN:
#             currval = float('inf')
#             for node in state.neighbors(MIN):
#                 val, state = self.minmax(node, state.next_player, depth - 1)
#                 if val < currval:
#                     currval = val
#                     beststate = node
#             return currval, beststate
#
#     def man_vs_ai(self, game, heuristic):
#         game.state.print()
#         move = choose_move()
#         game.make_move(move, MIN)
#         player = game.get_next_player()
#         while not game.no_moves():
#             game.state.print()
#             if player is MAX:
#                 val, move = self.minmax(game.state, player, heuristic)
#                 game.set_state(move)
#                 print("Value: "+str(val))
#             elif player is MIN:
#                 move = choose_move()
#                 game.make_move(move, player)
#             player = game.get_next_player()
#         game.state.print()
#         if game.winner():
#             print("Hai vinto")
#         elif game.draw():
#             print("Pareggio")
#         else:
#             print("Hai perso")
#
#     def ai_vs_ai(self, game, max_heuristic, min_heuristic):
#         game.state.print()
#         val, move = self.minmax(game.state, MIN)
#         game.state = move
#         player = game.get_next_player()
#         while not game.no_moves():
#             print("Value: " + str(val))
#             game.state.print()
#             if player is MAX:
#                 val, move = self.minmax(game.state, player, max_heuristic)
#             elif player is MIN:
#                 val, move = self.minmax(game.state, player, min_heuristic)
#             game.state = move
#             player = game.get_next_player()
#         game.state.print()
#         if game.winner():
#             print("Ha vinto MIN")
#         elif game.draw():
#             print("Pareggio")
#         else:
#             print("Ha vinto MAX")


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
    def alpha_beta(state, player, heuristic, max_player, min_player, alpha=float('-inf'), beta=float('inf'), depth=15):
        beststate = state
        if state.no_moves() or depth == 0:
            return heuristic.h(state, max_player), state

        if player is max_player:
            currval = float('-inf')
            for node in state.neighbors(player):
                val, state = SingleTurn.alpha_beta(
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
                val, state = SingleTurn.alpha_beta(
                    node, max_player, heuristic, max_player, min_player, alpha, beta, depth - 1)
                beta = min(beta, val)
                if val < currval:
                    currval = val
                    beststate = node
                if alpha >= beta:
                    break
            return currval, beststate

    def man_vs_ai(self, game, heuristic, depth):
        # make you play against an heuristic
        game.state.print()
        move = choose_move()
        game.make_move(move, MIN)
        player = MAX
        while not game.no_moves():
            # game loop
            game.state.print()
            if player is MAX:
                t = time()
                # ai player
                val, move = self.alpha_beta(game.state, player, heuristic, MAX, MIN, depth=depth)
                game.set_state(move)
                print("AI MOVE")
                print("Value: "+str(val))
                print("Move made in %s seconds" % (time()-t))
                player = MIN
            elif player is MIN:
                # human player
                move = choose_move()
                game.make_move(move, player)
                player = MAX

        game.state.print()
        if game.winner():
            print("You win!")
        elif game.draw():
            print("Draw!")
        else:
            print("You lose!")

    def ai_vs_ai(self, game, heuristic_1, heuristic_2, max_depth, min_depth):
        # make two heuristics play against each other
        game.state.print()
        val, move = self.alpha_beta(game.state, MIN, heuristic_1, MIN, MAX, depth=min_depth)
        game.state = move
        player = MAX
        start_time = time()
        while not game.no_moves():
            # game loop
            print("Value: " + str(val))
            game.state.print()
            if player is MAX:
                val, move = self.alpha_beta(game.state, player, heuristic_2, MAX, MIN, depth=max_depth)
            elif player is MIN:
                val, move = self.alpha_beta(game.state, player, heuristic_1, MIN, MAX, depth=min_depth)
            game.state = move
            if player is MAX:
                player = MIN
            elif player is MIN:
                player = MAX
        game.state.print()
        if game.winner():
            print("AI 1 wins")
        elif game.draw():
            print("Draw")
        else:
            print("AI 2 wins")
        print("Game ended in %s seconds" % (time()-start_time))


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
single_turn_game = SingleTurn()
# single_turn_game.man_vs_ai(mancala, SINGLE_TURN_RIGHT_H, 5)
single_turn_game.ai_vs_ai(mancala, SINGLE_TURN_PEBBLES_H, SINGLE_TURN_H, 5, 5)

