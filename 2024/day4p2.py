data = [list(line) for line in open("day4p2_input.txt").read().split("\n")]
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
count = 0

# def printGrid(grid, highlight_coords):
#     for i, row in enumerate(grid):
#         for j, cell in enumerate(row):
#             if (i, j) in highlight_coords:
#                 print(f"\033[43;30m{cell}\033[0m", end=" ")
#             else:
#                 print(cell, end=" ")
#         print()

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "A":
            diagCount = 0
            highlightCoords = []
            for dr, dc in directions:
                if 0 <= r - dr < len(data) and 0 <= c - dc < len(data[0]) \
                    and 0 <= r + dr < len(data) and 0 <= c + dc < len(data[0]):
                    if data[r - dr][c - dc] == "M" and data[r + dr][c + dc] == "S":
                        # highlightCoords.append((r - dr, c - dc))
                        # highlightCoords.append((r + dr, c + dc))
                        diagCount += 1
                
                if diagCount == 2:
                    # printGrid(data, highlightCoords)
                    count += 1         
                    break           
                    
print(count)