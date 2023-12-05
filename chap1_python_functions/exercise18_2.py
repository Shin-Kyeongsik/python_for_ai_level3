from utils2 import get_random_scores
from utils3 import cal_var

n_students = 10
scores = get_random_scores(n_students)
print(scores)

score_var = cal_var(scores)
print(f"{score_var = }")