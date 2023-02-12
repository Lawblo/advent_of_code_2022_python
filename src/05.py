from pprint import pprint 
input = open('../input/05.txt', 'r')
crates = []

for line in list(input)[0:8]:
    row = []
    for i in range(1, 34, 4): 
        row.append(line[i])
    crates.append(row)
    
crates.reverse()
columns = [[],[],[],[],[],[],[],[],[]]
for row in crates:
    for i in range(9):
        if row[i] != ' ':
            columns[i].append(row[i])

input.seek(0)

for line in list(input)[10:]:
    [_, num_move, _, from_move, _, to_move] = (line.strip().split())
    num_move = int(num_move)
    from_move = int(from_move) - 1
    to_move = int(to_move) - 1

    #for _ in range(num_move):
    #    moved_crate = columns[from_move].pop()
    #    columns[to_move].append(moved_crate)

    moved_crates = columns[from_move][-num_move:]
    del(columns[from_move][-num_move:])
    columns[to_move].extend(moved_crates)

final = ''

for row in columns:
    final += row[-1]
print(final)

input.close()
