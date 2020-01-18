from Game import MancalaGame
import Heuristics as H
from time import time
import Utils
import random

PL1 = 0
PL2 = 7

HP = H.RelativePointsHeuristic()
HB = H.PebblesHeuristic()
HR = H.RightCellHeuristic()


def man_vs_ai(game, heuristic, depth):
    # make you play against an heuristic
    # PL1 is human, PL2 is AI
    game.state.print()
    move = Utils.choose_move()
    game.make_move(move, PL1)
    player = PL2
    counter = 0
    while not game.no_moves():
        counter += 1
        # game loop
        game.state.print()
        if player is PL2:
            t = time()
            # ai player
            val, state = Utils.alpha_beta(game.state, player, heuristic, PL2, PL1, depth=depth)
            game.set_state(state)
            print("AI MOVE")
            print("Value: "+str(val))
            print("Move made in %s seconds" % (time()-t))
            player = PL1
        elif player is PL1:
            # human player
            move = Utils.choose_move()
            game.make_move(move, player)
            player = PL2

    game.state.print()
    if game.winner():
        print("You win!")
    elif game.draw():
        print("Draw!")
    else:
        print("You lose!")
    print("Game ended after %s moves" % counter)


def ai_vs_ai(game, heuristic_1, heuristic_2, pl1_depth, pl2_depth, print_game=True):
    # make two heuristics play against each other
    if print_game:
        game.state.print()
    # player 1 starts
    val, state = Utils.alpha_beta(game.state, PL1, heuristic_1, PL1, PL2, depth=pl1_depth)
    # val, move = Utils.media_max(game.state, PL1, heuristic_1, PL1, PL2, pl1_depth)
    game.set_state(state)
    player = PL2
    start_time = time()
    while not game.no_moves():
        # game loop
        if print_game:
            print("Value: " + str(val))
            game.state.print()

        # each player calls the alpha_beta function like he is the MAX player
        if player is PL2:
            val, state = Utils.alpha_beta(game.state, player, heuristic_2, PL2, PL1, depth=pl2_depth)
            # val, move = Utils.media_max(game.state, player, heuristic_2, PL2, PL1, depth=pl2_depth)
        elif player is PL1:
            val, state = Utils.alpha_beta(game.state, player, heuristic_1, PL1, PL2, depth=pl1_depth)
            # val, move = Utils.media_max(game.state, player, heuristic_1, PL1, PL2, depth=pl1_depth)

        game.set_state(state)
        if player is PL2:
            player = PL1
        elif player is PL1:
            player = PL2
    if print_game:
        game.state.print()
        print("Game ended in %s seconds" % (time()-start_time))
    if game.winner():
        print("AI 1 wins")
        return 1
    elif game.draw():
        print("Draw")
        return 0
    else:
        print("AI 2 wins")
        return 2


def coeff_train(game):
    coeff = [1, 1, 1]
    old_h = H.LinearCombinationHeuristic(coeff)
    pick = random.randint(0, 2)
    for i in range(0, 15):
        coeff[pick] += 1
        new_h = H.LinearCombinationHeuristic(coeff)
        pl1_score = 0
        pl2_score = 0
        print(coeff)
        print("--------------START GAME LOOP-----------------")
        for j in range(0, 10):
            print("----------------PLAY START-----------------")
            score = ai_vs_ai(game, new_h, old_h, 5, 5, False)
            if score == 1:
                pl1_score += 1
            elif score == 2:
                pl2_score += 2
            game.reset()

        if pl1_score > pl2_score:
            old_h = new_h
            print("PL1 wins")
        else:
            print("PL2 wins")
            new_pick = random.randint(0, 2)
            while new_pick == pick:
                new_pick = random.randint(0, 2)
            pick = new_pick
    print("--------------END GAME LOOP-------------------")
    print(coeff)
    return coeff


board = [4 for i in range(0, 6)]
board += [0]
board += [4 for j in range(0, 6)]
board += [0]
mancala = MancalaGame(board)
# coeff = coeff_train(mancala)
# HL = H.LinearCombinationHeuristic(coeff)
# mancala.reset()
ai_vs_ai(mancala, HP, HR, 3, 3)

