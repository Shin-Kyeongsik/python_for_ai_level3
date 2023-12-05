from utils import get_random_scores


def cal_mean(values):
    return sum(values) / len(values)


def cal_var(values, values_mean):
    squared_dev = []
    for value in values:
        squared_dev.append((value - values_mean)**2)
    var = cal_mean(squared_dev)
    return var


n_students, base_score = 100, 10
scores = get_random_scores(n_students)
score_mean = sum(scores) / len(scores)
score_var = cal_var(scores, score_mean)
print(f"{score_var = }")