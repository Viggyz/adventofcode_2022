import sys
sys.stdin = open('sample.in','r')

h = [0,0]
t = [0,0]

tail_positions = set()

mapping = {
    'U': [0,1],
    'R': [1,0],
    'D': [0,-1],
    'L': [-1,0]
}

try:
    while line:=input():
        action, steps = line.split(" ")
        for step in range(int(steps)):
            h[0] += mapping[action][0]
            h[1] += mapping[action][1]
            dx, dy = h[0]-t[0], h[1]-t[1]
            if abs(dx) == 0 and abs(dy) == 0:
                continue
            if abs(dx)>1 and abs(dy)>=1 or abs(dx)>=1 and abs(dy)>1:
                t[0] += 1 if dx > 0 else -1
                t[1] += 1 if dy > 0 else -1
            elif abs(dx)>1:
                t[0] += 1 if dx > 0 else -1
            elif abs(dy)>1:
                t[1] += 1 if dy > 0 else -1
            tail_positions.add(tuple(t))
except EOFError:
    print(tail_positions)
    print(len(tail_positions))

            
