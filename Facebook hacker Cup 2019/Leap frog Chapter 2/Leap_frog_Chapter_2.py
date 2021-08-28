
import math

def frog(line):
    length = len(line)
    if length > 2:
        min = math.floor(length / 2)
        B = line.count('B')
        if ((B >= 2) or (B >= min)) and (B <= (length-2)):
            return('Y')
        else:
            return('N')
    else:
        return('N')


with open('input.txt','r') as inf:
    T = int(inf.readline())

    for x in range(1,T+1):
        line = inf.readline().strip()
        result = frog(line)
        with open('output.txt', 'a') as outf:
            outf.write('Case #{}: {}\n'.format(x,result))


