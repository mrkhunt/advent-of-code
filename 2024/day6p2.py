data = [list(line) for line in open("day6p2_input.txt").read().split("\n")]

direction = "UP" # initial direction
row = len(data)
column = len(data[0])
startX, startY = 0, 0 # placeholder position

# find starting position
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            startX = i
            startY = j
            
def timeParadox(grid, x, y): 
    direction = "UP"
    seen = set()

    while True:
        seen.add((x, y, direction))
        if not ((0 <= x < row) and (0 <= y < column)):
            return False
        
        newX, newY = x, y
        
        if direction == "UP": newX -= 1
        elif direction == "RIGHT": newY += 1
        elif direction == "DOWN": newX += 1
        elif direction == "LEFT": newY -= 1
            
        if not ((0 <= newX < row) and (0 <= newY < column)):
            return False
        
        if grid[newX][newY] == "#":
            if direction == "UP": direction = "RIGHT"
            elif direction == "RIGHT": direction = "DOWN"
            elif direction == "DOWN": direction = "LEFT"
            elif direction == "LEFT": direction = "UP"
        else:
            x = newX
            y = newY
        
        if (x, y, direction) in seen:
            return True

obstacleCount = 0

for i in range(row):
    for j in range(column):
        if data[i][j] != ".":
            continue
        grid = [row[:] for row in data]
        grid[i][j] = "#"
        if timeParadox(grid, startX, startY): # Time Paradox
            obstacleCount += 1
        grid[i][j] = "."
            
print(obstacleCount)