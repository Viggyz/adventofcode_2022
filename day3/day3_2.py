import sys, re
sys.stdin = open('input.in', 'r')

sum = 0
try:
    while (line1:=input()) and (line2:=input()) and (line3:=input()):
        common = set(line1).intersection(set(line2).intersection(set(line3)))
        item = list(common)[0]
        # print(keys[ord(item) - ord('A')], item, min(list_first.count(item), list_sec.count(item)))
        # assert(list_first.count(item) < 5 or list_sec.count(item) < 5), f"{line}, {list_first.count(item)}, {list_sec.count(item)}"
        # print(item, keys[ord(item) - ord('A')])
        sum+= ord(item) - 97 + 1 if ord(item) > 90 else ord(item) - 65 + 27
except EOFError:
    print(sum)