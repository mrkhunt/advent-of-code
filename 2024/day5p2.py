data = open("day5p2_input.txt").read().split("\n\n")
rules = [tuple(line.split("|")) for line in data[0].split("\n")]
updates = [line.split(",") for line in data[1].split("\n")]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            for rule in rules:
                if arr[j] == rule[1] and arr[j+1] == rule[0]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

middleSum = 0

for update in updates:
    sortedUpdate = update.copy()
    bubbleSort(sortedUpdate)
    if sortedUpdate != update:
        # Not Sorted
        middleSum += int(sortedUpdate[(len(sortedUpdate))//2])
    else:
        # Sorted Already
        continue

print(middleSum)



# Incorrect.... Can't create a global sort (because of circular dependencies)
# first create a simple ordering based on the rules for the pairs
# Go with an O(n^2) approach to compare all pairs of numbers in the update

'''
allNumsList = []
for update in updates:
    for num in update:
        if num not in allNumsList:
            allNumsList.append(num)
 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            for rule in rules:
                if arr[j] == rule[1] and arr[j+1] == rule[0]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sortedList = bubbleSort(allNumsList)
middleSum = 0

for update in updates:
    globalIndex = 0
    correctOrder = True
    for num in update:
        while globalIndex < len(sortedList) and num != sortedList[globalIndex]:
            globalIndex += 1
        if not globalIndex < len(sortedList) or num != sortedList[globalIndex]:
            correctOrder = False
            break
    if correctOrder:    
        middleSum += int(update[(len(update))//2])

print(middleSum)
'''
