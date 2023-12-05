import random


def get_random_scores(n_students):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores


def cal_score_mean(scores):
    score_mean = sum(scores) / len(scores)
    return score_mean


def cal_score_max(scores):
    max_score = None
    for score in scores:
        if max_score == None or score > max_score:
            max_score = score
    return max_score


def cal_score_min(scores):
    min_score = None
    for score in scores:
        if min_score == None or score < min_score:
            min_score = score
    return min_score


def cal_divisors(num):
    divisors = []
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors