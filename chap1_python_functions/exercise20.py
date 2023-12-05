from utils2 import cal_divisors


def is_prime(num):
    divisors = cal_divisors(num)
    if len(divisors) == 2:
        IS_PRIME = True
    else:
        IS_PRIME = False
    return IS_PRIME


num = int(input("Enter a number: "))
print(f"Is {num} a prime number? {is_prime(num)}")