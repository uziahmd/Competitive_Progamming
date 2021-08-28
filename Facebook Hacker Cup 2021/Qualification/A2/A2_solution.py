def turns(line, trans, common):
    result = []
    print(common)
    for a in common:
        paths = []
        temp = []
        temp.append(a)
        paths.append(temp)
        count = 0
        for x in trans:
            if temp[-1] == x[1]:
                count = count + 1
        for x in range(count-1):
            paths.append(temp)
        
        for current in paths:
            for x in trans:
                if x[1] == current[-1]:
                    current.append(x[0])
        print(paths)
            # count = 0
            # for current in paths:
            #     if x[1] == current[-1]:
            #         if count == 0:
            #             current.append(x[0])
            #             count = count + 1
            #         else:
            #             print("yeet")
            #             paths.append(current)
        #print(paths)

def possible(line, trans):
    all_combin = []
    the_set =set()
    for x in line:
        the_set.add(x)
    for x in the_set:
        temp = []
        temp.append(x)
        all_combin.append(temp)
    
    for a in trans:
        for x in all_combin:
            if a[0] in x:
                x.append(a[1])
    for a in all_combin:
        for x in all_combin:
            if a[0] in x:
                x.extend(a)
    
    combin_set = []
    for x in all_combin:
        combin_set.append(set(x))
    
    common = combin_set[0]
    for x in combin_set[1:]:
        common.intersection_update(x)
    # print(the_set)
    # print(combin_set)
    return common


def min_time(line, n_trans, trans):
    length = len(line)
    print(line)
    common = possible(line, trans)
    if len(common) == 0:
        print("-1")
    elif(n_trans == 0):
        print(0)
    else: 
        turns(line, trans, common)

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