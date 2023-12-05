import random


def get_randint_data(min, max, n_data):
    data = [random.randint(min, max) for _ in range(n_data)]
    return data


def cal_unique_values(data, return_cnts):
    cnt_dict = {}
    for data_ in data:
        cnt_dict[data_] = cnt_dict.get(data_, 0) + 1

    if return_cnts:
        return list(cnt_dict.keys()), list(cnt_dict.values())
    else:
        return list(cnt_dict.keys())


data = get_randint_data(0, 10, 1000)

unique_values = cal_unique_values(data, False)
print(f"{unique_values = }\n")

unique_values, unique_cnts = cal_unique_values(data, True)
print(f"{unique_values = }")
print(f"{unique_cnts = }")