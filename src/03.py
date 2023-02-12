from string import ascii_letters
input = open('../input/03.txt', 'r')

priority = {}

for letter in ascii_letters:
    if ord(letter) > 90:
        priority[letter] = ord(letter) - 96
    else:
        priority[letter] = ord(letter) - 38 

def part1():
    total = 0
    for line in input: 
        backpack = line.strip()
        mid = len(backpack) // 2
        comp1, comp2 = backpack[mid:], backpack[:mid]

        common = None

        for letter in comp1:
            if letter in comp2:
                common = letter

        total += priority[common]

    print(total)
def part2():
    total = 0
    group = []
    for line in input:

        backpack = line.strip()

        group.append(backpack)

        if len(group) == 3:
            elf1, elf2, elf3 = group

            for letter in elf1:
                if letter in elf2 and letter in elf3:
                    total += (priority[letter])
                    break
            group = []
    print(total)

part2()



input.close()
