from collections import defaultdict

# def printGrid(grid, highlight_coords):
#     for i, row in enumerate(grid):
#         for j, cell in enumerate(row):
#             if (i, j) in highlight_coords:
#                 print(f"\033[43;30m{cell}\033[0m", end=" ")
#             else:
#                 print(cell, end=" ")
#         print()

data = [list(line) for line in open("day8p2_input.txt").read().split("\n")]
symbolPositions = defaultdict(list)
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] != ".": symbolPositions[data[r][c]].append((r,c))
antinodeSet = set()

for symbol, positions in symbolPositions.items():
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            pointOne_x, pointOne_y = positions[i][0], positions[i][1]
            pointTwo_x, pointTwo_y = positions[j][0], positions[j][1]
            
            slopeX = pointTwo_x - pointOne_x
            slopeY = pointTwo_y - pointOne_y
            
            k = 0
            while True:
                antinode = (pointOne_x - k*slopeX, pointOne_y - k*slopeY)
                
                k += 1

                if not (antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(data) or antinode[1] >= len(data[0])):
                    antinodeSet.add(antinode)
                else:
                    break
                
            k = 0
            while True:
                antinode = (pointTwo_x + k*slopeX, pointTwo_y + k*slopeY)
                k += 1

                if not (antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(data) or antinode[1] >= len(data[0])):
                    antinodeSet.add(antinode)
                else:
                    break

# printGrid(data, antinodeSet)
print(len(antinodeSet))