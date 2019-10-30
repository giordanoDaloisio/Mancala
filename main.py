from Game import MancalaGame
import Heuristics as H
from time import time
import Utils

MIN = 0
MAX = 7

HP = H.RelativePointsHeuristic()
HB = H.PebblesHeuristic()
HR = H.RightCellHeuristic()


def man_vs_ai(game, heuristic, depth):
    # make you play against an heuristic
    game.state.print()
    move = Utils.choose_move()
    game.make_move(move, MIN)
    player = MAX
    counter = 0
    while not game.no_moves():
        counter += 1
        # game loop
        game.state.print()
        if player is MAX:
            t = time()
            # ai player
            val, move = Utils.alpha_beta(game.state, player, heuristic, MAX, MIN, depth=depth)
            game.set_state(move)
            print("AI MOVE")
            print("Value: "+str(val))
            print("Move made in %s seconds" % (time()-t))
            player = MIN
        elif player is MIN:
            # human player
            move = Utils.choose_move()
            game.make_move(move, player)
            player = MAX

    game.state.print()
    if game.winner():
        print("You win!")
    elif game.draw():
        print("Draw!")
    else:
        print("You lose!")
    print("Game ended after %s moves" % counter)


def ai_vs_ai(game, heuristic_1, heuristic_2, max_depth, min_depth):
    # make two heuristics play against each other
    game.state.print()
    val, move = Utils.alpha_beta(game.state, MIN, heuristic_1, MIN, MAX, depth=min_depth)
    game.state = move
    player = MAX
    start_time = time()
    while not game.no_moves():
        # game loop
        print("Value: " + str(val))
        game.state.print()
        if player is MAX:
            val, move = Utils.alpha_beta(game.state, player, heuristic_2, MAX, MIN, depth=max_depth)
        elif player is MIN:
            val, move = Utils.alpha_beta(game.state, player, heuristic_1, MIN, MAX, depth=min_depth)
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


board = [4 for i in range(0, 6)]
board += [0]
board += [4 for i in range(0, 6)]
board += [0]
mancala = MancalaGame(board)
#man_vs_ai(mancala, HP, 5)
ai_vs_ai(mancala, HR, HB, 5, 5)

