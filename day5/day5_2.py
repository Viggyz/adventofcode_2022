import sys, re
sys.stdin = open('input.in', 'r')

# stacks = [[], ['Z','N'],['M','C','D'],['P']]
# [H]                 [Z]         [J]
# [L]     [W] [B]     [G]         [R]
# [R]     [G] [S]     [J] [H]     [Q]
# [F]     [N] [T] [J] [P] [R]     [F]
# [B]     [C] [M] [R] [Q] [F] [G] [P]
# [C] [D] [F] [D] [D] [D] [T] [M] [G]
# [J] [C] [J] [J] [C] [L] [Z] [V] [B]
# [M] [Z] [H] [P] [N] [W] [P] [L] [C]
stacks = [
    [],
    ['M','J','C','B','F','R','L','H'],
    ['Z','C','D'],
    ['H','J','F','C','N','G','W'],
    ['P','J','D','M','T','S','B'],
    ['N','C','D','R','J'],
    ['W','L','D','Q','P','J','G','Z'],
    ['P','Z','T','F','R','H'],
    ['L','V','M','G'],
    ['C','B','G','P','F','Q','R','J'],
]

pattern = re.compile(r'move (\b\d+\b) from (\b\d+\b) to (\b\d+\b)')

while input():
    continue

try:
    while line:=input():
        match = pattern.search(line)
        move_count, from_, to = map(int, match.groups())
        stacks[to].extend(stacks[from_][-move_count:])
        del stacks[from_][-move_count:]
except EOFError:
    print("".join([stack.pop() for stack in stacks if len(stack)!=0]))
