from utils import get_random_scores


def cal_pass_scores_mean(scores, threshold, pass_type):
    target_scores = []
    for score in scores:
        if pass_type == 'pass' and score >= threshold:
            target_scores.append(score)
        elif pass_type == 'no pass' and score < threshold:
            target_scores.append(score)

    mean = sum(target_scores) / len(target_scores)
    return mean


n_students, threshold = 100, 80
scores = get_random_scores(n_students)

pass_scores_mean = cal_pass_scores_mean(scores, threshold, 'pass')
no_pass_scores_mean = cal_pass_scores_mean(scores, threshold, 'no pass')
print(f"pass scores mean: {pass_scores_mean:.2f}")
print(f"no pass scores mean: {no_pass_scores_mean:.2f}")