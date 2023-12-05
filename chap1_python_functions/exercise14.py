from utils2 import get_random_scores


def cal_score_mean(scores):
    score_mean = sum(scores) / len(scores)
    return score_mean


n_students = 10
scores = get_random_scores(n_students)
print(f"{scores = }")

score_mean = cal_score_mean(scores)
print(f"{score_mean = }")