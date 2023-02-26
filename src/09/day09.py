# Rope Bridge

def read_input():
    return list(open('./09.txt', 'r'))
    # return ['U 5']


visited = [[0, 0]]


def part1():
    rope = {'head': [0, 0], 'tail': [0, 0]}
    # input = read_input()

    for line in input:
        handle_line(rope, line.rstrip())


def part2():
    input = read_input()
    rope = [[0, 0] for i in range(10)]
    for line in input:
        handle_line(rope, line.rstrip())

    print(rope)


def handle_line(rope, command):
    direction, amount = command.split()
    direction = direction.lower()
    amount = int(amount)
    for i in range(amount):
        handle_action_p2(rope, direction)


def handle_action_p2(rope, direction):
    for index in range(len(rope)):
        coordinate = rope[index]
        if index == 0:
            rope[0] = perform_move(coordinate, direction)
        else:
            difference = find_difference(rope[index-1], rope[index])
            if difference_move_needed(difference):
                handled_difference = handle_difference(difference, rope[index])
                rope[index] = handled_difference
        if index == 9:
            mark_visited(rope[index])


def difference_move_needed(difference) -> bool:
    if 2 in difference or -2 in difference:
        return True
    else:
        return False


def handle_difference(difference, tail):
    move = ''
    match difference:
        case [2, 1]:
            move = 'ur'
        case [2, 2]:
            move = 'ur'
        case [1, 2]:
            move = 'ur'
        case [0, 2]:
            move = 'u'
        case [-2, 1]:
            move = 'ul'
        case [-1, 2]:
            move = 'ul'
        case [-2, 2]:
            move = 'ul'
        case [-2, 0]:
            move = 'l'
        case [-2, -1]:
            move = 'dl'
        case [-1, -2]:
            move = 'dl'
        case [-2, -2]:
            move = 'dl'
        case [0, -2]:
            move = 'd'
        case [2, -1]:
            move = 'dr'
        case [1, -2]:
            move = 'dr'
        case [2, -2]:
            move = 'dr'
        case [2, 0]:
            move = 'r'
    performed_move = perform_move(tail, move)
    return performed_move


def find_difference(head, tail): return [head[0] - tail[0], head[1] - tail[1]]


def perform_move(position, move):
    match move:
        case 'r': return [position[0]+1, position[1]]
        case 'l': return [position[0]-1, position[1]]
        case 'u': return [position[0], position[1]+1]
        case 'd': return [position[0], position[1]-1]
        case 'ul': return [position[0]-1, position[1]+1]
        case 'ur': return [position[0]+1, position[1]+1]
        case 'dl': return [position[0]-1, position[1]-1]
        case 'dr': return [position[0]+1, position[1]-1]


def mark_visited(location):
    global visited
    if location not in visited:
        visited.append(location)


def handle_action(rope, direction):
    head = rope['head']
    tail = rope['tail']
    new_head = perform_move(head, direction)
    new_tail = tail
    difference = find_difference(new_head, tail)
    if difference_move_needed(difference):
        new_tail = handle_difference(difference, tail)
        mark_visited(new_tail)

    rope['head'] = new_head
    rope['tail'] = new_tail


part2()
