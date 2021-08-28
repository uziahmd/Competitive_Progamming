def min_time(line, n_tras, trans):
    length = len(line)
    print(line)
    print(length)
    print(n_trans)
    print(trans)

with open('input.txt','r') as inf:
    T = int(inf.readline())
    for x in range(1,T+1):
        line = inf.readline().strip()
        n_trans = int(inf.readline())
        trans = []
        for x in range(0, n_trans):
            trans[x] = inf.readline().strip()

        min_time(line, n_trans, trans)
        # with open('output.txt', 'a') as outf:
        #      outf.write('Case #{}: {}\n'.format(x,result))