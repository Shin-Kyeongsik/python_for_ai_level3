from utils3 import get_random_scores


def cal_mean(values):
    sum_ = 0
    for value in values:
        sum_ += value
    mean = sum_ / len(values)
    return mean


scores = get_random_scores()
mean = cal_mean(scores) # BP
print(f"{mean = }")