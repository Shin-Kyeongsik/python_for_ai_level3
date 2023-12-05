from utils3 import get_random_scores


def print_mean(values):
    sum_ = 0
    for value in values:
        sum_ += value
    mean = sum_ / len(values)
    print(f"mean: {mean}")


scores = get_random_scores()
print_mean(scores) # BP