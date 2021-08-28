def Mr_X(line):
    length=len(line)
    if length == 1:
        if (line == 'x') or (line == 'X'):
            return(1)
        else:
            return(0)
    else:
         if eval(line.replace('x','1').replace('X','0')) == eval(line.replace('x','0').replace('X','1')):
             return(0)
         else:
             return(1)

with open('input.txt','r') as inf:
    T = int(inf.readline())

    for x in range(1,T+1):
        line = inf.readline().strip()
        result = Mr_X(line)
        with open('output.txt', 'a') as outf:
            outf.write('Case #{}: {}\n'.format(x,result))
