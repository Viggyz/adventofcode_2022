import sys, re
from collections import deque
sys.stdin = open('input.in', 'r')

cycle_queue = deque()
cycle = 1
x = 1

VIEW_CYCLES = {20, 60, 100, 140, 180, 220}
total = 0

try:
    while line:=input():
        if pattern:=re.search(r'addx (-?\d+)', line):
            value, = map(int, pattern.groups())
            cycle_queue.append(None)
            cycle_queue.append(value)
        else:
            cycle_queue.append(None)
        while len(cycle_queue):
            if cycle in VIEW_CYCLES:
                print(f"{cycle}th cycle, signal stregth = {cycle*x}, X = {x}")
                total += cycle*x
            if value := cycle_queue.popleft():
                x += value
            cycle += 1
        
except EOFError:
    print(f"Total={total}")
    print(total)