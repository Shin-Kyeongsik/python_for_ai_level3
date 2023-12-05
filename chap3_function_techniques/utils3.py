import random


def get_random_scores(n_students=100):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores