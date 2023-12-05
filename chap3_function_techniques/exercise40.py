from utils import get_random_scores, cal_pass_scores_mean

n_students, threshold = 100, 80
scores = get_random_scores(n_students=n_students)

pass_score_mean = cal_pass_scores_mean(scores=scores, threshold=threshold,
                                       pass_type='pass')
no_pass_score_mean = cal_pass_scores_mean(scores=scores, threshold=threshold,
                                          pass_type='no pass')
print(f"{pass_score_mean = :.2f}")
print(f"{no_pass_score_mean = :.2f}")