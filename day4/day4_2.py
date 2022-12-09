import sys
sys.stdin = open('input.in', 'r')

try:    
    running_sum = 0
    while line:=input():
        first, sec = line.split(",")
        one_1, one_2= map(int, first.split('-'))
        two_1, two_2 = map(int, sec.split('-'))
        one, two = set(range(one_1, one_2+1)), set(range(two_1, two_2+1))
        if one.intersection(two):
            running_sum += 1
except EOFError:
    print(running_sum)