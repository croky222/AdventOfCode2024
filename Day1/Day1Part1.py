import pandas as pd
list = pd.read_csv("C:\\Users\\cnegrea\\PycharmProjects\\AdventOfCode2024\\Day1\\Day1input.txt", sep="   ")

list1 = sorted(list.l1)
list2 = sorted(list.l2)

pairlist = []
distance = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        pairlist.append((list1[i],list2[i]))
        if list1[i] > list2[i]:
            distance.append(list1[i] - list2[i])
        else:
            distance.append(list2[i] - list1[i])

print(sum(distance))


