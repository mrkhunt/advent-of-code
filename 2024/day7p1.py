data = open("day7p1_input.txt").read().split("\n")

sum = 0

for equation in data:
    equation = equation.split(":")
    testValue = int(equation[0])
    testNumbers = [int(i) for i in equation[1].split()]
    def evalSum(testValue, testNumbers):
        if len(testNumbers) == 1:
            if testValue == testNumbers[0]:
                return True
            else:
                return False
        else:
            if evalSum(testValue, [testNumbers[0]*testNumbers[1]] + testNumbers[2:]): return True
            elif evalSum(testValue, [testNumbers[0]+testNumbers[1]] + testNumbers[2:]): return True
            else: return False
    
    if evalSum(testValue, testNumbers):
        sum += testValue
    
print(sum)