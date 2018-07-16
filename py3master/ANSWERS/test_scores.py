#!/usr/bin/env python

scores = {}
scores_total = 0

with open("../DATA/testscores.dat") as f:

    for line in f:
        (name,score) = line.split(":")
        score = int(score)
        scores[name] = score
        scores_total += score

for student, score in sorted(scores.items()):
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
    print("{0:<20s} {1} {2}".format(student,scores[student],grade))

average = float(scores_total)/len(scores)
print("\naverage score is  {0:.2f}\n".format(average))
