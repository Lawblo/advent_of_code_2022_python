input = open('../input/04.txt', 'r')

def part1():
    overlaps = 0
    overlaps2 = 0
    for line in input:
        section1, section2 = line.strip().split(',')
        section1 = list(map(int, section1.split('-')))
        section2 = list(map(int, section2.split('-')))

        if section1[0] >= section2[0] and section1[1] <= section2[1]:
            overlaps += 1
        elif section2[0] >= section1[0] and section2[1] <= section1[1]:
            overlaps += 1


        #for num in range(section1[0], section1[1] + 1):
        #    if num in range(section2[0], section2[1] + 1):
        #        overlaps2 += 1
        s1 = set(range(section1[0], section1[1] + 1))
        s2 = set(range(section2[0], section2[1] + 1))
        if s1.intersection(s2):
            overlaps2 += 1


    print(overlaps2)
part1()
input.close()
