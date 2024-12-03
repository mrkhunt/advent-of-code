data = open("day1p2_input.txt").read().split()
list1 = []
list2 = {}

for i in range(len(data)):
    if(i%2 == 0):
        list1.append(data[i])
    else:
        if str(data[i]) not in list2:
            list2[str(data[i])] = 1
        else:
            list2[str(data[i])] += 1

similarity = 0

for i in range(len(list1)):
    similarity += int(list1[i]) * int(list2[str(list1[i])] if str(list1[i]) in list2 else 0)

print(similarity)