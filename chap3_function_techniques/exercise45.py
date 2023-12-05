import random


def get_randint_data(min, max, n_data):
    data = [random.randint(min, max) for _ in range(n_data)]
    return data


def cal_unique_values(data, return_cnts=False):
    cnt_dict = {}
    for data_ in data:
        cnt_dict[data_] = cnt_dict.get(data_, 0) + 1

    if return_cnts:
        return list(cnt_dict.keys()), list(cnt_dict.values())
    else:
        return list(cnt_dict.keys())


data = get_randint_data(min=0, max=10, n_data=1000)

print(cal_unique_values(data=data))
print(cal_unique_values(data=data, return_cnts=True))