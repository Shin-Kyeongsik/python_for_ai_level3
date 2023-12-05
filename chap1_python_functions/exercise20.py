from utils2 import cal_divisors


def is_prime(num):
    divisors = cal_divisors(num)
    if len(divisors) == 2:
        return True
    else:
        return False


num = int(input("Enter a number: "))
print(f"Is {num} a prime number? {is_prime(num)}")