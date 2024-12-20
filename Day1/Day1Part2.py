import pandas as pd
list = pd.read_csv("C:\\Users\\cnegrea\\PycharmProjects\\AdventOfCode2024\\Day1\\Day1input.txt", sep="   ")

similarity_score = []
for i in list['l1']:
    howmany_times_appears = list['l2'][list['l2'] == i].count()
    similarity_score.append(i * howmany_times_appears)


print(sum(similarity_score))