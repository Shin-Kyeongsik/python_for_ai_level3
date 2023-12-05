from utils2 import get_random_scores
from utils3 import cal_mean


def cal_var(values):
    mean = cal_mean(values)
    squared_dev = [(value - mean)**2 for value in values]

    var = cal_mean(squared_dev)
    return var


n_students = 10
scores = get_random_scores(n_students)
print(scores)

score_var = cal_var(scores)
print(f"{score_var = }")