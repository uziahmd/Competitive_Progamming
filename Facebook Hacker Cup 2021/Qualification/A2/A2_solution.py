def final_paths(trans, paths):
    temp = paths.copy()

def make_graph(trans):
    graph = [[999]*26]*26
    for x in trans:
        graph[ord(x[0])-65][ord(x[1])-65] = 1
    
    return graph

def dist(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def turns(line, trans, common):
    graph = make_graph(trans)
    shortest = dist(graph)
    paths = []
    for x in range(26):
        temp = 0
        for y in line:
            temp = temp + shortest[ord(y)-65][x]
        paths.append(temp)
    print(paths)
    return min(paths)

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
        print(turns(line, trans, common))

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