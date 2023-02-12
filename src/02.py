input = open('../input/02.txt', 'r')

part1_score = {('A', 'X'): 4,
               ('B', 'X'): 1,
               ('C', 'X'): 7,
               ('A', 'Y'): 8,
               ('B', 'Y'): 5,
               ('C', 'Y'): 2,
               ('A', 'Z'): 3,
               ('B', 'Z'): 9,
               ('C', 'Z'): 6
              }

loss = 0
draw = 3
win = 6

rock = 1
paper = 2
scissors = 3

part2_score = {('A', 'X'): scissors + loss,
               ('A', 'Y'): rock + draw,
               ('A', 'Z'): paper + win,
               ('B', 'X'): loss + rock,
               ('B', 'Y'): draw + paper,
               ('B', 'Z'): win + scissors,
               ('C', 'X'): loss + paper,
               ('C', 'Y'): draw + scissors,
               ('C', 'Z'): win + rock
              }

def get_score(results):

    total = 0

    for line in input:
        round = tuple(line.split())
        total += results[round]

    print(total)

get_score(part2_score)


input.close()

