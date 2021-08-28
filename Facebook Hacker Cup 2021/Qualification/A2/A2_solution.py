def trans_combi(line, trans):
    trans_copy = trans[:]
    all_combin = []
    theset =set()
    print(trans)
    for x in trans:
        theset.add(x[0])
    print(theset)



def min_time(line, n_trans, trans):
    length = len(line)
    print(line)
    print(n_trans)
    trans_combi(line, trans)

with open('input.txt','r') as inf:
    T = int(inf.readline())
    for x in range(1,T+1):
        line = inf.readline().strip()
        n_trans = int(inf.readline())
        trans = []
        for x in range(n_trans):
            trans.append(inf.readline().strip())

        min_time(line, n_trans, trans)
        # with open('output.txt', 'a') as outf:
        #      outf.write('Case #{}: {}\n'.format(x,result))