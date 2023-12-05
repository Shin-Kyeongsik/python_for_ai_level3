from utils import get_random_scores
from utils2 import cal_mean


def mean_subtraction(values):
    mean = cal_mean(values)

    values = values.copy()
    for idx in range(len(values)):
        values[idx] -= mean
    return values


n_students = 100
scores = get_random_scores(n_students=n_students)
score_mean = cal_mean(values=scores)
print(f"mean before ms: {score_mean:.2f}")

scores_ms = mean_subtraction(values=scores)
score_mean_ms = cal_mean(values=scores_ms)
print(f"mean after ms: {score_mean_ms:.2f}")