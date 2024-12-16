import os

data = [list(line) for line in open("day6p1_input.txt").read().split("\n")]

direction = "UP" # initial direction
row = len(data)
column = len(data[0])
x, y = 0, 0 # placeholder position

# find starting position
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            x = i
            y = j

while (0 <= x < row) and (0 <= y < column):
    data[x][y] = "X"
    if direction == "UP":
        if x-1 >= 0 and data[x-1][y] == "#":
            direction = "RIGHT"
        else:
            x -= 1
    elif direction == "RIGHT":
        if y+1 < column and data[x][y+1] == "#":
            direction = "DOWN"
        else:
            y += 1
    elif direction == "DOWN":
        if x+1 < row and data[x+1][y] == "#":
            direction = "LEFT"
        else:
            x += 1
    elif direction == "LEFT":
        if y >= 0 and data[x][y-1] == "#":
            direction = "UP"
        else:
            y -= 1
    # print(x, y)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("\n".join(" ".join(map(str, row)) for row in data))


count = 0
for i in range(row):
    for j in range(column):
        if data[i][j] == "X":
            count += 1
            
print(count)