import random


def get_random_scores(n_students):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores


n_students = 10
scores = get_random_scores(10)
print(scores)