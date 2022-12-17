ROUNDS = 10000
LVL_RED = 1

# monkeys = [
#     {
#         'items': [79, 98],
#         'op': lambda old: old * 19,
#         'test': lambda x: 2 if x%23==0 else 3,
#         'mod': 23,
#         'insp_count': 0
#     },
#     {
#         'items': [54, 65, 75, 74],
#         'op': lambda old: old + 6,
#         'test': lambda x: 2 if x%19==0 else 0,
#         'mod': 19,
#         'insp_count': 0
#     },
#     {
#         'items': [79, 60, 97],
#         'op': lambda old: old * old,
#         'test': lambda x: 1 if x%13==0 else 3,
#         'mod': 13,
#         'insp_count': 0
#     },
#     {
#         'items': [74],
#         'op': lambda old: old + 3,
#         'test': lambda x: 0 if x%17==0 else 1,
#         'mod': 17,
#         'insp_count': 0
#     },
# ]
# 
monkeys = [
    {
        'items': [59, 74, 65, 86],
        'op': lambda old: old * 19,
        'test': lambda x: 6 if x%7==0 else 2,
        'mod': 7,
        'insp_count': 0
    },
    {
        'items': [62, 84, 72, 91, 68, 78, 51],
        'op': lambda old: old + 1,
        'test': lambda x: 2 if x%2==0 else 0,
        'mod': 2,
        'insp_count': 0
    },
    {
        'items': [78, 84, 96],
        'op': lambda old: old + 8,
        'test': lambda x: 6 if x%19==0 else 5,
        'mod': 19,
        'insp_count': 0
    },
    {
        'items': [97, 86],
        'op': lambda old: old * old,
        'test': lambda x: 1 if x%3==0 else 0,
        'mod': 3,
        'insp_count': 0
    },
    {
        'items': [50],
        'op': lambda old: old + 6,
        'test': lambda x: 3 if x%13==0 else 1,
        'mod': 13,
        'insp_count': 0
    },
    {
        'items': [73, 65, 69, 65, 51],
        'op': lambda old: old * 17,
        'test': lambda x: 4 if x%11==0 else 7,
        'mod': 11,
        'insp_count': 0
    },
    {
        'items': [69, 82, 97, 93, 82, 84, 58, 63],
        'op': lambda old: old + 5,
        'test': lambda x: 5 if x%5==0 else 7,
        'mod': 5,
        'insp_count': 0
    },
    {
        'items': [81, 78, 82, 76, 79, 80],
        'op': lambda old: old + 3,
        'test': lambda x: 3 if x%17==0 else 4,
        'mod': 17,
        'insp_count': 0
    },
]

new_worry = None

lcm = 1
for monkey in monkeys:
    lcm *= (lcm*monkey['mod'])

for i in range(ROUNDS):
    for monkey in monkeys:
        monkey['insp_count'] += len(monkey['items'])
        while len(monkey['items']) and (item:=monkey['items'].pop()):
            new_worry = monkey['op'](item)
            new_monkey_index = monkey['test'](new_worry)
            monkeys[new_monkey_index]['items'].append(new_worry%lcm)

monkeys = sorted(monkeys, key=lambda monkey: monkey['insp_count'], reverse=True)
print(monkeys[0]['insp_count'] * monkeys[1]['insp_count'])
