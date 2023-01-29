def calculation_avg(*args):
    sum_unit, sum_score = 0, 0
    for score in args:
        sum_unit += score[1]
        sum_score += score[0] * score[1]
    return sum_score/sum_unit