lines = None
with open('input.in', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

dir_mapping = ((-1, 0), (0, 1), (1, 0), (0, -1)) 
visible_hash = (0x1000, 0x0100, 0x0010, 0x0001)
invisible_hash = (0x2000, 0x0200, 0x0020, 0x0002)
# 0 unchecked, 1 visible, 2 invisible

visibility = [[0x0000 for _ in range(len(lines))] for _ in  range(len(lines))]

def check_visibility(row, col, dir_index, direction):
    x, y = direction
    if row==0 or col==0 or row==len(lines)-1 or col==len(lines)-1:
        visibility[row][col] ^= visible_hash[dir_index]
        return True
    elif int(lines[row][col]) <= int(lines[row + x][col + y]):
        visibility[row][col] ^= invisible_hash[dir_index]
        return False
    else:
        trow, tcol = row + x, col + y
        while 0<=trow<len(lines) and 0<=tcol<len(lines[0]):
            if int(lines[row][col]) <= int(lines[trow][tcol]):
                visibility[row][col] ^= invisible_hash[dir_index]
                return False
            else:
                trow += x
                tcol += y
        visibility[row][col] ^= visible_hash[dir_index]
        return True



visible_tree_count = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        for index, direction in enumerate(dir_mapping):
            check_visibility(row, col, index, direction)
        if visibility[row][col] != 0x2222:
            visible_tree_count +=1
print(visibility)
print(visible_tree_count)
                
    
                
