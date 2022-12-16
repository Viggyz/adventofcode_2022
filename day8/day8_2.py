lines = None
with open('input.in', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

dir_mapping = ((-1, 0), (0, 1), (1, 0), (0, -1)) 
visibility = [[0x0000 for _ in range(len(lines))] for _ in  range(len(lines))]

top_score = 1
for row in range(1,len(lines)-1):
    for col in range(1,len(lines[0])-1):
        score = 1
        px, py = row, col
        for index, (dx,dy) in enumerate(dir_mapping):
            mx, my = row + dx, col + dy
            loc_score = 0
            while 0<=mx<len(lines) and 0<=my<len(lines[0]):
                loc_score += 1
                if lines[row][col] <= lines[mx][my]:
                    break
                else:
                    mx += dx
                    my += dy
            score *= loc_score
        top_score = max(score, top_score)
print(top_score)  