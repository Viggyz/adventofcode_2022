import sys, re
sys.stdin = open('day2.in', 'r')

score = (1,2,3)
select_mapping = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
matchup_mapping = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    },
}

total_score = 0
play = 0
try:
    while line:= input():
        opp, self = line.split()
        matchup_score = matchup_mapping[opp][self]
        choice_score:int = select_mapping[self]
        print(matchup_score, choice_score)
        total_score += (choice_score + matchup_score)
except EOFError:
    print(total_score)