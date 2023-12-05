import random


def get_randint_data(min=0, max=100, n_data=100):
    data = [random.randint(min, max) for _ in range(n_data)]
    return data


data = get_randint_data()
print(f"mean:", sum(data) / len(data))

data = get_randint_data(min=50)
print(f"mean:", sum(data) / len(data))

data = get_randint_data(max=50)
print(f"mean:", sum(data) / len(data))

data = get_randint_data(min=40, max=60)
print(f"mean:", sum(data) / len(data))

data = get_randint_data(min=30, max=60, n_data=1000)
print(f"{len(data) = }")
print(f"mean:", sum(data) / len(data))