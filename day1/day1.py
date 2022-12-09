import sys, re
sys.stdin = open('day1.in', 'r')
# sys.stdout = open('day2.out', 'w')
import heapq
from functools import reduce

try:
    list_ = []
    highest = 0
    running_sum = 0
    while (line:=input())!= None:
        if line=="":
            heapq.heappush(list_, -running_sum)
            running_sum = 0
        else:
            running_sum += int(line)
except EOFError:
    print(reduce(lambda running, new: running - new,  (heapq.heappop(list_) for _ in range(3)), 0))