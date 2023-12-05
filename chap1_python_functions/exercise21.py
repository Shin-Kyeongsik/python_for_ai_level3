from utils2 import get_random_scores, cal_score_mean

n_students = 100
scores = get_random_scores(n_students)
score_mean = cal_score_mean(scores)
print(f"scores before ms: {scores}")
print(f"mean before ms: {score_mean:.2f}\n")

for score_idx in range(len(scores)):
    scores[score_idx] -= score_mean

score_mean = cal_score_mean(scores)
print(f"scores after ms: {scores}")
print(f"mean after ms: {score_mean:.2f}")