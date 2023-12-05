from utils import get_random_scores


def cal_pass_scores_mean(scores, threshold):
    pass_scores = []
    for score in scores:
        if score >= threshold:
            pass_scores.append(score)
    pass_score_mean = sum(pass_scores) / len(pass_scores)
    return pass_score_mean


n_students, threshold = 100, 80
scores = get_random_scores(n_students)

pass_score_mean = cal_pass_scores_mean(scores, threshold)
print(f"{pass_score_mean = }")