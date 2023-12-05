import datetime


def print_score_mean(scores):
    score_mean = sum(scores) / len(scores)
    print(f"score mean: {score_mean}")


def print_score_max_min(scores):
    score_max, score_min = None, None
    for score in scores:
        if score_max == None or score > score_max:
            score_max = score

        if score_min == None or score < score_min:
            score_min = score
    print(f"score max / min: {score_max} / {score_min}")


def start_end_time(type):
    if type == 'start':
        print(f"START at {datetime.datetime.now()}")
    elif type == 'end':
        print(f"END at {datetime.datetime.now()}")
    else:
        print("WARNING: Unknown type")