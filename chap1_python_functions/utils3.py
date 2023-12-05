from utils2 import cal_divisors


def cal_sum(values):
    sum_ = 0
    for value in values:
        sum_ += value
    return sum_


def cal_mean(values):
    sum_ = cal_sum(values)
    mean = sum_ / len(values)
    return mean


def cal_var(values):
    mean = cal_mean(values)
    squared_dev = [(value - mean)**2 for value in values]

    var = cal_mean(squared_dev)
    return var


def cal_std(scores):
    var = cal_var(scores)
    return var**0.5


def is_prime(num):
    divisors = cal_divisors(num)
    if len(divisors) == 2:
        IS_PRIME = True
    else:
        IS_PRIME = False
    return IS_PRIME
