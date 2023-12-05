from utils import get_random_scores


def cal_mean(scores, base_score=0):
    score_sum = 0
    for score in scores:
        score_sum += score + base_score
    score_mean = score_sum / len(scores)
    return score_mean


n_students = 100
scores = get_random_scores(n_students=n_students)

print(f"{cal_mean(scores=scores)}") # BP
print(f"{cal_mean(scores=scores, base_score=10)}")
print(f"{cal_mean(scores=scores, base_score=20)}")