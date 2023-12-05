from utils2 import get_random_scores


def cal_score_max(scores):
    max_score = None
    for score in scores:
        if max_score == None or score > max_score:
            max_score = score
    return max_score


def cal_score_min(scores):
    min_score = None
    for score in scores:
        if min_score == None or score < min_score:
            min_score = score
    return min_score


n_students = 10
scores = get_random_scores(n_students)
print(f"{scores = }")

max_score, min_score = cal_score_max(scores), cal_score_min(scores)
print(f"{max_score = } / {min_score = }")
