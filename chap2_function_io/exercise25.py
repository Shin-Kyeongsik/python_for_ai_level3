from utils import get_random_scores


def cal_mean_adjusted(scores, base_score):
    score_sum = 0
    for score in scores:
        score_sum += score + base_score
    score_mean = score_sum / len(scores)
    return score_mean


n_students, base_score = 100, 10
scores = get_random_scores(n_students)

print(f"{cal_mean_adjusted(scores, 0) = }")
print(f"{cal_mean_adjusted(scores, 10) = }")
print(f"{cal_mean_adjusted(scores, 20) = }")