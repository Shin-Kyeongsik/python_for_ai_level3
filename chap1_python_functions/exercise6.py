import random


def print_score_mean(scores):
    score_mean = sum(scores) / len(scores)
    print(f"score mean: {score_mean}")


n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

print_score_mean(scores) # BP