from utils2 import get_random_scores
from utils3 import cal_std

n_students = 10
scores = get_random_scores(n_students)
print(scores)

score_std = cal_std(scores)
print(f"{score_std = :.2f}")