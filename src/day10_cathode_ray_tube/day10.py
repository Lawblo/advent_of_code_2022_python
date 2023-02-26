def get_input():
    return list(open('./day10_data.txt'))


input_1 = get_input()
signal_strength = []
cycle = 0
x_reg = 1


def run_command(input_line):
    global cycle, x_reg
    command, *V = input_line.split()
    if len(V) > 0:
        V = int(V[0])
    if command == 'noop':
        run_cycle(1, 0)
    else:
        run_cycle(2, V)
        x_reg += V


def run_cycle(amount, V):
    global cycle
    for i in range(amount):
        check_cycle(V)


def check_cycle(V):
    global cycle, x_reg, signal_strength
    cycle += 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_strength.append(x_reg*cycle)


for line in input_1:
    run_command(line.rstrip())


print(signal_strength)
