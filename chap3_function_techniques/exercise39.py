from utils import get_random_scores, cal_max_min

n_students = 100
scores = get_random_scores(n_students=n_students)

max_value, max_idx, min_value, min_idx = cal_max_min(values=scores, return_idx=True)
print(f"max / max_idx: {max_value} / {max_idx}")
print(f"min / min_idx: {min_value} / {min_idx}")