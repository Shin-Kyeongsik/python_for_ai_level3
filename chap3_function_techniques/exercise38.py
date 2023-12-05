from utils import get_random_scores, cal_mean_adjusted

n_students, base_score = 100, 20
scores = get_random_scores(n_students=n_students)

score_mean = cal_mean_adjusted(scores=scores, base_score=0)
score_mean_adjusted = cal_mean_adjusted(scores=scores, base_score=base_score)
print(f"{score_mean = }")
print(f"{score_mean_adjusted = }")