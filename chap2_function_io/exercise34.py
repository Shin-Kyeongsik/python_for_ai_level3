from utils import get_random_scores


def cal_statistics(values, return_data):
    sum_ = 0
    for value in values:
        sum_ += value
    if return_data == 'sum': return sum_

    mean = sum_ / len(values)
    if return_data == 'mean': return mean

    squared_dev = []
    for value in values:
        squared_dev.append((value - mean)**2)
    var = sum(squared_dev) / len(values)
    if return_data == 'var': return var

    std = var**0.5
    if return_data == 'std': return std

    if return_data == 'all':
        return sum_, mean, var, std


n_students = 100
scores = get_random_scores(n_students)
print(cal_statistics(scores, 'sum'))
print(cal_statistics(scores, 'mean'))
print(cal_statistics(scores, 'var'))
print(cal_statistics(scores, 'std'))
print(cal_statistics(scores, 'all'))