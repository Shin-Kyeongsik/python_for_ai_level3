import random


def print_score_max_min(scores):
    score_max, score_min = None, None
    for score in scores:
        if score_max == None or score > score_max:
            score_max = score

        if score_min == None or score < score_min:
            score_min = score
    print(f"score max / min: {score_max} / {score_min}")


n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

print_score_max_min(scores) # BP