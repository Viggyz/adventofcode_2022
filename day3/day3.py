import sys, re
sys.stdin = open('input.in', 'r')

keys = (27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
        0,0,0,0,0,0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)

sum = 0
try:
    while line:=input():
        assert(len(line)%2==0)
        length = len(line)
        list_first, list_sec = line[:(length//2)], line[length//2:]
        first_half, sec_half = set(line[:(length//2)]), set(line[length//2:])
        assert(len(line[:(length//2)])+len(line[length//2:])==len(line)), f"{len(line[:(length//2)])},{len(line[length//2:])},{len(line)}"
        assert(len(list(first_half.intersection(sec_half)))==1)
        item = list(first_half.intersection(sec_half))[0]
        # print(keys[ord(item) - ord('A')], item, min(list_first.count(item), list_sec.count(item)))
        assert(list_first.count(item) < 5 or list_sec.count(item) < 5), f"{line}, {list_first.count(item)}, {list_sec.count(item)}"
        print(item, keys[ord(item) - ord('A')])
        sum += keys[ord(item) - ord('A')]
except EOFError:
    print(sum)