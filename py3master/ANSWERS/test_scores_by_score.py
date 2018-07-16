#!/usr/bin/env python

scores_of = {}
score_total = 0

with open("../DATA/testscores.dat") as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores_of[name] = score
        score_total += score

for student, score in sorted(scores_of.items(), key=lambda e: (e[1]),
                             reverse=True):
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    print("{0:<20s} {1:2d} {2}".format(student, score, grade))

average = float(score_total) / len(scores_of)
print("\naverage score is  {0:.2f}\n".format(average))
