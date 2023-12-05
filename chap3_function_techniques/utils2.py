def cal_mean(values):
    mean = sum(values) / len(values)
    return mean


def cal_std(values):
    mean = cal_mean(values)
    squared_dev = [(value - mean)**2 for value in values]
    var = cal_mean(squared_dev)

    std = var**0.5
    return std


def cal_vec_norm(vec):
    vec_norm = 0
    for element in vec:
        vec_norm += element**2
    vec_norm **= 0.5
    return vec_norm


def cal_max_min(values, return_idx=False):
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
        return {'max': max_value, 'min': min_value,
                'max_idx': max_idx, 'min_idx': min_idx}
    else:
        return {'max': max_value, 'min': min_value}