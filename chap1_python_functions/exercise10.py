import random
from utils import print_score_mean, print_score_max_min

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

print_score_mean(scores) # BP
print_score_max_min(scores)