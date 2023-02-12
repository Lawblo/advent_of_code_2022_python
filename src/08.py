from pprint import pprint
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
    left = line[:x]
    return left

def get_right(line, x):
    right = line[x+1:]
    return right

def get_above(input, x, y):
    above = []
    for line in input[:y]:
        above.append(line[x])
    return above

def get_below(input, x, y):
    below = []
    for line in input[y+1:]:
        below.append(line[x])
    return below

def part2_data(input):
    tree_hash = {}

    for y in range(len(input)):
        for x in range(len(input[y])):
            tree_hash[(x, y)] = {
                    'node': input[y][x],
                    'above': get_above(input, x, y),
                    'below': get_below(input, x, y),
                    'left': get_left(input[y], x),
                    'right': get_right(input[y], x),
                    'scenic': 0
                    }

    return tree_hash

def part2_solve(data):
    size = int(math.sqrt(len(data)))
    for y in range(size):
        for x in range(size):
            tree = data[(x, y)]
            print(tree)

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
    data = part2_data(test_input)
    part2_solve(data)
