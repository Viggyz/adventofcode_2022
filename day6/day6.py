import sys
sys.stdin = open('input.in','r')

line = input()
OFFSET = 4

for index in range(len(line)-OFFSET):
    if len(set(line[index:index+OFFSET]))==OFFSET:
        print(index+OFFSET)
        break
