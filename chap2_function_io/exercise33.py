from utils import get_random_scores


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
        return max_value, min_value
    else:
        return max_value, max_idx, min_value, min_idx


n_students = 100
scores = get_random_scores(n_students)
print(cal_max_min(scores, return_idx=True))
print(cal_max_min(scores, return_idx=False))