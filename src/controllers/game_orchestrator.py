from src.utilities.score_type import *


class ScoreBoard:
    SCORE_SHEET = {ONES: None, TWOS: None, THREES: None}
    TOTAL_SCORE = 0

    def play(self, roll, score_type):
        score = calculate_score(roll, score_type)
        self.TOTAL_SCORE += score
        self.SCORE_SHEET[score_type] = score

