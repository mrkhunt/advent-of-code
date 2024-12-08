data = [list(line) for line in open("day4p1_input.txt").read().split("\n")]
directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
word = "XMAS"
count = 0

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == word[0]:
            for dr, dc in directions:
                matchCount = 0
                for i in range(len(word)):
                    if 0 <= r + dr*i < len(data) and 0 <= c + dc*i < len(data[0]):
                        if data[r + dr*i][c + dc*i] == word[i]:
                            matchCount += 1
                            
                if matchCount == len(word):
                    count += 1                    
                    
print(count)