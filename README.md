# Mancala python artificial agent

To play the game run

`python main.py`

In the main.py file uncomment `man_vs_ai(mancala, HP, 5)` to play against the computer or uncomment `ai_vs_ai(mancala, HR, HB, 5, 5)` to see the heuristics play against each other.

Possible heuristics are:
- HP: Relative points heuristic
- HB: Opponent pebbles heuristic
- HR: Right most cell heuristic

The last value of the function is the deep of the AI
