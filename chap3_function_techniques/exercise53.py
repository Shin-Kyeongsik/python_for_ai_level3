from utils import get_random_scores
from utils2 import cal_max_min


def sort_values(data, descending=True):
    data_sort = []
    data = data.copy()
    for _ in range(n_students):
        max_min_dict = cal_max_min(values=data, return_idx=True)
        if descending:
            target_value, target_idx = max_min_dict['max'], max_min_dict['max_idx']
        else:
            target_value, target_idx = max_min_dict['min'], max_min_dict['min_idx']
        data_sort.append(target_value)
        data.pop(target_idx)
    return data_sort


n_students = 20
scores = get_random_scores(n_students=n_students)
print(scores, '\n')

print(sort_values(data=scores))
print(sort_values(data=scores, descending=False))