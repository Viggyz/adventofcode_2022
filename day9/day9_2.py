import sys
sys.stdin = open('input.in','r')

h = [[0,0] for _ in range(10)]

tail_positions = set()

mapping = {
    'U': [0,1],
    'R': [1,0],
    'D': [0,-1],
    'L': [-1,0]
}

def move_knots(index):
    dx, dy = h[index-1][0]-h[index][0], h[index-1][1]-h[index][1]
    if abs(dx) == 0 and abs(dy) == 0:
        return
    if abs(dx)>1 and abs(dy)>=1 or abs(dx)>=1 and abs(dy)>1:
        h[index][0] += 1 if dx > 0 else -1
        h[index][1] += 1 if dy > 0 else -1
    elif abs(dx)>1:
        h[index][0] += 1 if dx > 0 else -1
    elif abs(dy)>1:
        h[index][1] += 1 if dy > 0 else -1

try:
    while line:=input():
        action, steps = line.split(" ")
        for step in range(int(steps)):
            h[0][0] += mapping[action][0]
            h[0][1] += mapping[action][1]
            
            for i in range(1,10):
                move_knots(i)
            tail_positions.add(tuple(h[9]))
except EOFError:
    print(tail_positions)
    print(len(tail_positions))

            
