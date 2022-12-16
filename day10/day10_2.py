import sys, re
from collections import deque
sys.stdin = open('input.in', 'r')

cycle_queue = deque()
cycle = 1
x = 1

image = ""

try:
    while line:=input():
        if pattern:=re.search(r'addx (-?\d+)', line):
            value, = map(int, pattern.groups())
            cycle_queue.append(None)
            cycle_queue.append(value)
        else:
            cycle_queue.append(None)
        while len(cycle_queue):
            if x-1<=(cycle-1)%40<=x+1:
                image += "#"
            else: 
                image += "."
            if cycle%40==0:
                # print(f"{cycle}th cycle, signal stregth = {cycle*x}, X = {x}")
                image +="\n"
            if value := cycle_queue.popleft():
                x += value
            cycle += 1
        
except EOFError:
    print(image)