import random
import utils

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

utils.print_score_mean(scores) # BP
utils.print_score_max_min(scores)