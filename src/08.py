from pprint import pprint
import numpy
import math

input = list(map(str.rstrip, open('../input/08.txt', 'r')))
'''height & width = 99'''

test_input = ['30373', '25512', '65332', '33549', '35390']

def visible_horizontal(line, index):
    left = line[:index]
    node = int(line[index])
    right = line[index+1:]
    visible_left = not any(int(x) >= node for x in left)
    visible_right = not any(int(x) >= node for x in right)
    visible = visible_left or visible_right
    return visible_left or visible_right


def visible_vertical(input, x, y):
    node = int(input[y][x])
    above = get_above(input, x, y)
    below = get_below(input, x, y)
    visible_above = not any(int(x) >= node for x in above)
    visible_below = not any(int(x) >= node for x in below)
    visible = visible_above or visible_below
    return visible

def get_left(line, x):

    left = map(int, line[:x])
    return left

def get_right(line, x):
    right = map(int, line[x+1:])
    return right

def get_above(input, x, y):
    above = []
    for line in input[:y]:
        above.append(int(line[x]))
    return above

def get_below(input, x, y):
    below = []
    for line in input[y+1:]:
        below.append(int(line[x]))
    return below

def part2_data(input):
    tree_hash = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            tree = {
                    'node': int(input[y][x]),
                    'above': list(get_above(input, x, y)),
                    'below': list(get_below(input, x, y)),
                    'left': list(get_left(input[y], x)),
                    'right': list(get_right(input[y], x)),
                    'scenic': 0
                    }

            if tree['left'] and len(tree['left']) > 1:
                tree['left'].reverse()

            if tree['above'] and len(tree['above']) > 1:
                tree['above'].reverse()

            tree_hash[(x, y)] = tree


    return tree_hash

def part2_solve(data):
    most_scenic = data[(0, 0)]
    size = int(math.sqrt(len(data)))
    for y in range(size):
        for x in range(size):
            tree = data[(x, y)]
            get_scenic(tree)
            if tree['scenic'] > most_scenic['scenic']:
                most_scenic = tree

    pprint(most_scenic)
    
#TODO: reverse left (and top?)
def get_scenic(tree):
    most_scenic = [0, 0, 0, 0]
    directions = [tree['left'], tree['above'], tree['right'], tree['below']]
    for index, direction in enumerate(directions):
        for height in direction:
            most_scenic[index] = most_scenic[index] + 1
            if height >= tree['node']:
                break
    tree['scenic'] = most_scenic[0] * most_scenic[1] * most_scenic[2] * most_scenic[3]
    print(tree)
    print(most_scenic)


def part1(input):
    tree_hash = {}

    for i in range(len(input)):
        for j in range(len(input[i])):
            tree = input[i][j]
            vis_h = visible_horizontal(input[i], j)
            vis_v = visible_vertical(input, j, i)
            
            tree_hash[(i,j)] = {'tree': tree, 'visible': False}

            if vis_h or vis_v:
                tree_hash[(i,j)]['visible'] = True

    visible_trees = 0
    for tree, value in tree_hash.items():
        if value['visible'] == True:
            visible_trees += 1
    print(visible_trees)

if __name__ == "__main__":
    data = part2_data(input)
    part2_solve(data)
