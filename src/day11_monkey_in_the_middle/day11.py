from functools import reduce

import re
from pprint import pprint

with open('./data.txt') as file:
    input = file.read()


test_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkeys[j] 2
    If false: throw to monkeys[j] 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkeys[j] 2
    If false: throw to monkeys[j] 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkeys[j] 1
    If false: throw to monkeys[j] 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkeys[j] 0
    If false: throw to monkeys[j] 1
'''

monkeys = []
for index, monkey in enumerate(test_input.split('\n\n')):
    if len(monkey) == 0:
        break
    lines = monkey.split('\n')

    monkeys.append({
        'items': [int(x) for x in re.findall(r'\d+', lines[1])],
        'op': re.search(r'([*+])\s+(\w+)', lines[2]).groups(),
        'test_divisible': int(re.search(r'\d+', lines[3]).group()),
        'test_true':    int(re.search(r'\d+', lines[4]).group()),
        'test_false': int(re.search(r'\d+', lines[5]).group()),
        'items_inspected': 0
    })


def handle_operation(item, op):
    num = op[1]
    if num == 'old':
        num = item
    else:
        num = int(num)

    if op[0] == '*':
        return item * num
    return item + num


dividers = [monkey['test_divisible'] for monkey in monkeys]
modulo = reduce(lambda x, y: x * y, dividers, 1)

for i in range(10000):
    j = i % len(monkeys)
    while len(monkeys[j]['items']) > 0:
        item = monkeys[j]['items'].pop(0) % modulo
        item = handle_operation(item, monkeys[j]['op'])
        test = item % monkeys[j]['test_divisible'] == 0
        if test:
            pass_to = monkeys[j]['test_true']
        else:
            pass_to = monkeys[j]['test_false']
        monkeys[pass_to]['items'].append(item)
        monkeys[j]['items_inspected'] += 1

items_passed = [monkey['items_inspected'] for monkey in monkeys]
items_passed.sort()
print(items_passed[-1] * items_passed[-2])
