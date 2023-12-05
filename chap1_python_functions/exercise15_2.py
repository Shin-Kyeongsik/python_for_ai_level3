from utils2 import (get_random_scores,
                    cal_score_max, cal_score_min)

n_students = 10
scores = get_random_scores(n_students)
print(f"{scores = }")

max_score, min_score = cal_score_max(scores), cal_score_min(scores)
print(f"{max_score = } / {min_score = }")
