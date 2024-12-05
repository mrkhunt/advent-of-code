data = [list(map(int, line.split())) for line in open("day2p2_input.txt").read().split("\n")]

count = 0

for original_report in data:
    for i in range(len(original_report)):
        report = original_report[:i] + original_report[i+1:]
        differences = [report[j] - report[j-1] for j in range(1, len(report))]
        increasing = sum(1 <= diff <= 3 for diff in differences)
        decreasing = sum(-3 <= diff <= -1 for diff in differences)
        if increasing >= (len(differences)) or decreasing >= (len(differences)):
            count += 1
            break
        
print(count)

