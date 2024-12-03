data = open("day1p1_input.txt").read().split()
list1 = []
list2 = []

for i in range(len(data)):
    if(i%2 == 0):
        list1.append(data[i])
    else:
        list2.append(data[i])

list1.sort()
list2.sort()

distance = 0

for i in range(len(list1)):
    distance += abs(int(list1[i]) - int(list2[i]))

print(distance)