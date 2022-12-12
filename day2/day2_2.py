import sys
sys.stdin = open('day2.in', 'r')

select_mapping = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}
matchup_mapping = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2,
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3,
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1,
    },
}

total_score = 0
play = 0
try:
    while line:= input():
        opp, self = line.split()
        matchup_score = matchup_mapping[opp][self]
        choice_score:int = select_mapping[self]
        total_score += (choice_score + matchup_score)
except EOFError:
    print(total_score)