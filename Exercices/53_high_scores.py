# Exercise 53: Filter High Scores
# Objective: Practice filtering items from a list into a new list.

score_list = [45, 88, 72, 95, 60]

def get_high_score(scores, threshold):
    high_scores = []
    for score in scores:
        if score >= threshold:
            high_scores.append(score)
    return high_scores

print(get_high_score(score_list, 80))
