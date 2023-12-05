from utils2 import get_random_scores
from utils3 import cal_mean

n_students = 10
scores = get_random_scores(n_students)

score_mean = cal_mean(scores)
print(f"{score_mean = }")