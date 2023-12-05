from utils import get_random_scores, cal_max_min


def cal_max_min(values):
    max_value = cal_max_min(values, 'max')
    min_value = cal_max_min(values, 'min')
    return max_value, min_value


n_students = 100
scores = get_random_scores(n_students)
max_score, min_score = cal_max_min(scores)
print(f"max / min: {max_score} / {min_score}")