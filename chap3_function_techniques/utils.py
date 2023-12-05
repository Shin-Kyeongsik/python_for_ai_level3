import random


def get_random_scores(n_students):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores


def cal_mean_adjusted(scores, base_score):
    score_sum = 0
    for score in scores:
        score_sum += score + base_score
    score_mean = score_sum / len(scores)
    return score_mean


def cal_max_min(values, return_idx):
    max_value, max_idx = None, None
    min_value, min_idx = None, None
    for idx, value in enumerate(values):
        if max_value == None or value > max_value:
            max_value = value
            max_idx = idx

        if min_value == None or value < min_value:
            min_value = value
            min_idx = idx

    if return_idx:
        return max_value, max_idx, min_value, min_idx
    else:
        return max_value, min_value


def cal_pass_scores_mean(scores, threshold, pass_type):
    target_scores = []
    for score in scores:
        if pass_type == 'pass' and score >= threshold:
            target_scores.append(score)
        elif pass_type == 'no pass' and score < threshold:
            target_scores.append(score)

    mean = sum(target_scores) / len(target_scores)
    return mean