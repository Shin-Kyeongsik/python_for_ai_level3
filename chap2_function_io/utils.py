import random


def get_random_scores(n_students):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores


def cal_max_min(values, max_min):
    target_value = None
    if max_min == 'max':
        for value in values:
            if target_value == None or value > target_value:
                target_value = value
    elif max_min == 'min':
        for value in values:
            if target_value == None or value < target_value:
                target_value = value
    return target_value


def cal_pass_scores_mean(scores, threshold, pass_type):
    target_scores = []
    for score in scores:
        if pass_type == 'pass' and score >= threshold:
            target_scores.append(score)
        elif pass_type == 'no pass' and score < threshold:
            target_scores.append(score)

    mean = sum(target_scores) / len(target_scores)
    return mean