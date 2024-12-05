import re

data = open("day3p2_input.txt").read()
pattern = r'do\(\)|don\'t\(\)|mul\(-?\d{1,3},-?\d{1,3}\)'
matches = re.findall(pattern, data)
sum = 0
do = True

for match in matches:
    if(match == "do()"):
        do = True
        continue
    elif(match == "don't()"):
        do = False
        continue
    elif do:
        pair = match[4:-1].split(",")
        sum += (int(pair[0]) * int(pair[1]))
    
print(sum)