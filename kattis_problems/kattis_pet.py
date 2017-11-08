scores = []
for i in range(5):
    temp = 0
    temp_scores = input().split()
    for scor in temp_scores:
        temp += int(scor)
    scores.append(temp)

winner = max(scores)
print("{0} {1}".format(scores.index(winner)+1, winner))
