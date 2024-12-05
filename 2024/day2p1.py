data = [list(map(int, line.split())) for line in open("day2p1_input.txt").read().split("\n")]

count = 0

for report in data:
    differences = [report[j] - report[j-1] for j in range(1, len(report))]
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    if increasing or decreasing:
        count += 1
        
print(count)
