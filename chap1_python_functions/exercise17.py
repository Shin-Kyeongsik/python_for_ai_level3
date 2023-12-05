from utils2 import get_random_scores


def cal_sum(values):
    sum_ = 0
    for value in values:
        sum_ += value
    return sum_


def cal_mean(values):
    sum_ = cal_sum(values)
    mean = sum_ / len(values)
    return mean


n_students = 10
scores = get_random_scores(n_students)

score_mean = cal_mean(scores)
print(f"{score_mean = }")