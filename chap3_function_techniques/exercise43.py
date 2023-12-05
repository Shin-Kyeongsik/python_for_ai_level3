from utils import get_random_scores


def cal_pass_score_mean(scores, threshold=80):
    pass_scores = []
    for score in scores:
        if score >= threshold:
            pass_scores.append(score)

    pass_score_mean = sum(pass_scores) / len(pass_scores)
    return pass_score_mean


n_students, threshold = 100, 80
scores = get_random_scores(n_students=n_students)

pass_score_mean = cal_pass_score_mean(scores=scores)
print(f"{pass_score_mean = :.2f}")

pass_score_mean = cal_pass_score_mean(scores=scores, threshold=70)
print(f"{pass_score_mean = :.2f}")

pass_score_mean = cal_pass_score_mean(scores=scores, threshold=50)
print(f"{pass_score_mean = :.2f}")