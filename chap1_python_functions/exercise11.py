import random
from utils import (print_score_mean, print_score_max_min,
                   start_end_time)

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

start_end_time('start')
print_score_mean(scores)
print_score_max_min(scores)
start_end_time('end')