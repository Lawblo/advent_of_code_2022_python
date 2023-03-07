def get_input():
    return list(open('./day10_data.txt'))


input_1 = get_input()
signal_strength = []
cycle = 0
x_reg = 1


def run_command(input_line: str):
    global x_reg
    command, *V = input_line.split()
    if len(V) > 0:
        V = int(V[0])
    if command == 'noop':
        run_cycle(1)
    else:
        run_cycle(2)
        x_reg = x_reg + V


def run_cycle(amount):
    for _ in range(amount):
        check_cycle()


def check_cycle():
    global cycle, x_reg, signal_strength
    cycle += 1
    print(x_reg)
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_strength.append(x_reg*cycle)


# for line in input_1:
#    run_command(line.rstrip())

input_2 = list(open('./day10_data.txt'))
crt_rows = []


def part2():
    while input_2:
        if len(input_2) < 1:
            break

        for row in range(1, 7):
            if len(input_2) < 1:
                break

            draw_row = ['.' for _ in range(40)]
            for px in range(40):
                if len(input_2) < 1:
                    break

                line = input_2.pop(0)
                draw_row = handle_cycle(line, px, draw_row)


def handle_cycle(line, px, draw_row):
    global x_reg
    command, *V = line.split()
    if len(V) > 0:
        V = int(V[0])

    if x_reg == px+1:
        draw_row[px+1] = 'X'
    elif x_reg == px-1:
        draw_row[px-1] = 'X'
    elif x_reg == px:
        draw_row[px] = 'X'
    return draw_row


part2()
