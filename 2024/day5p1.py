data = open("day5p2_input.txt").read().split("\n\n")
rules = [line.split("|") for line in data[0].split("\n")]
updates = [line.split(",") for line in data[1].split("\n")]

middleSum = 0

for update in updates:
    seenSet = set()
    correctUpdate = True
    for num in update:
        for rule in rules:
            if num in rule[0]:
                # confirm rule[1] is not seen so far
                if rule[1] in seenSet:
                    correctUpdate = False
                    break
            elif num in rule[1]:
                # confirm rule[0] has to be seen if it is in update
                if rule[0] in update and rule[0] not in seenSet: 
                    correctUpdate = False
                    break
        if correctUpdate:
            # confirm all rules seen for num
            # add num in seenSet
            seenSet.add(num)
        else:
            break
    if correctUpdate:
        middleSum += int(update[(len(update))//2])
        
print(middleSum)