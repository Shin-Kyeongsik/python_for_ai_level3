from utils2 import get_random_scores, cal_score_mean
from utils3 import cal_std

n_students = 100
scores = get_random_scores(n_students)
score_mean = cal_score_mean(scores)
score_std = cal_std(scores)
print(f"scores before ms: {scores}")
print(f"mean / std before ms: {score_mean:.2f} / {score_std:.2f}\n")

for score_idx, score in enumerate(scores):
    scores[score_idx] = (score - score_mean) / score_std

score_mean = cal_score_mean(scores)
score_std = cal_std(scores)
print(f"scores after ms: {scores}")
print(f"mean / std before ms: {score_mean:.2f} / {score_std:.2f}")