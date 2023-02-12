'''
start of packet is indicated by four different characters
part1: find index of first packet
'''
input = list(open('../input/06.txt', 'r'))[0].strip()

for i in range(len(input)):
    current_block = input[i:i+14]
    if len(set(current_block)) == 14:
        print(i+14)
        break
