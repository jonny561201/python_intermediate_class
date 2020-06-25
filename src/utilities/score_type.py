from src.utilities import die_scoring

ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'


def calculate_score(list_die, score_type):
    if score_type == ONES:
        die_scoring.score_ones(list_die)
    elif score_type == TWOS:
        die_scoring.score_twos(list_die)
    elif score_type == THREES:
        die_scoring.score_threes(list_die)