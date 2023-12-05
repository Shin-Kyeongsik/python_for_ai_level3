from utils import get_random_scores
from utils2 import cal_sum, cal_mean, cal_var, cal_std


def cal_statistics(values):
    sum_ = cal_sum(values)
    mean = cal_mean(values)
    var = cal_var(values)
    std = cal_std(values)
    return sum_, mean, var, std


n_students = 100
scores = get_random_scores(n_students)

score_sum, score_mean, score_var, score_std = cal_statistics(scores)
print(f"{score_sum = }")
print(f"{score_mean = }")
print(f"{score_var = }")
print(f"{score_std = }")