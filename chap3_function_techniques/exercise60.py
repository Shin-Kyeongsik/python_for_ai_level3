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


if __name__ == '__main__':
    from utils3 import get_random_scores

    scores = get_random_scores()
    print(cal_max_min(values=scores, return_idx=True))