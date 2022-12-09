import sys
sys.stdin = open('input.in', 'r')

try:    
    running_sum = 0
    while line:=input():
        first, sec = line.split(",")
        one_1, one_2= map(int, first.split('-'))
        two_1, two_2 = map(int, sec.split('-'))
        # assert(one_1!=two_1 and one_2!=two_2), f"{one_1},{two_1},{one_2},{two_2}"
        if (
            (one_1>=two_1 and one_2<=two_2)
            or (one_1<=two_1 and one_2>=two_2)
        ):
            running_sum += 1
except EOFError:
    print(running_sum)