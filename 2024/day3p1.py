import re

data = open("day3p1_input.txt").read()
pattern = r'mul\(-?\d{1,3},-?\d{1,3}\)'
matches = re.findall(pattern, data)
sum = 0

for match in matches:
    pair = match[4:-1].split(",")
    sum += (int(pair[0]) * int(pair[1]))
    
print(sum)