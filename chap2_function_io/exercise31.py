from utils import get_random_scores, cal_pass_scores_mean


def pass_no_pass_means(scores, threshold):
    pass_score_mean = cal_pass_scores_mean(scores, threshold, 'pass')
    no_pass_score_mean = cal_pass_scores_mean(scores, threshold, 'no pass')
    return pass_score_mean, no_pass_score_mean


n_students, threshold = 100, 80
scores = get_random_scores(n_students)

pass_score_mean, no_pass_score_mean = pass_no_pass_means(scores, threshold)
print(f"{pass_score_mean = :.2f}")
print(f"{no_pass_score_mean = :.2f}")