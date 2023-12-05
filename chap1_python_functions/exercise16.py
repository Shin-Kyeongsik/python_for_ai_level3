def cal_divisors(num):
    divisors = []
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors


num = int(input("Enter a number: "))
print(f"divisors of {num} is {cal_divisors(num)}")