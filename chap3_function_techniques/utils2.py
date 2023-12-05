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