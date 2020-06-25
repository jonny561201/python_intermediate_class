from random import randint

from src.controllers.game_orchestrator import ScoreBoard
from src.utilities.score_type import ONES, TWOS


def roll():
    return [__roll_one_die(), __roll_one_die(), __roll_one_die(), __roll_one_die(), __roll_one_die()]


def __roll_one_die():
    return randint(1, 6)


score_board = ScoreBoard()
first_roll = roll()
print(first_roll)
score_board.play(first_roll, ONES)
print(score_board.TOTAL_SCORE)

score_board.play(roll(), TWOS)
print(score_board.TOTAL_SCORE)



    # We are just building the scoring component
    # given a list of 5 die also what we are scoring for 1,2,3 etc
    # we have to take those and score them
        # 1,2,3,4,5,6
        # 3 of kind, 4 of a kind
        # full house, small straight, large straight, yahtzee, wild

    #1. walk through how we need to keep track of keeping score between rolls
    #2. therefore we need to build a object/class to keep track
    #3. We have all the functions built out and no classes
    #4. Start with unit testing scoring as there are defects
    #5. Once we have the application tested build out a class to keep track of score
    #6. Call it from here at the top of the app