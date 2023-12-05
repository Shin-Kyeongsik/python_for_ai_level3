def get_sum_upto_n(n):
    sum_ = 0
    for num in range(1, n + 1):
        sum_ += num
    return sum_


print(get_sum_upto_n(5))
print(get_sum_upto_n(10))
print(get_sum_upto_n(20))