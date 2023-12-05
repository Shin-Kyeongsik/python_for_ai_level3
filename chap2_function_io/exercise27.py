from utils import get_random_scores


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


n_students = 100
scores = get_random_scores(n_students)
max_score = cal_max_min(scores, 'max')
min_score = cal_max_min(scores, 'min')

print(f"{max_score = }")
print(f"{min_score = }")