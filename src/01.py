file = map(lambda x: x.strip(), (open('../input/01.txt', 'r')))

elves = []
elf_inv = []


for line in file:
    if len(line) < 1:
        elves.append(sum(elf_inv))
        elf_inv = []
    else:
        elf_inv.append(int(line))
    

top = []
for i in range(3):
    top.append(elves.pop((elves.index(max(elves)))))

print(sum(top))



