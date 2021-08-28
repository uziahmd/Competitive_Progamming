def min_time(line):
    length = len(line)

    if length == 1:
        return 0

    alpha_set = set()
    for x in range (length):
        alpha_set.add(line[x])
    
    vowel = set("AEIOU")
    v_count= [0]
    c_count = [0]
    for a in alpha_set:
        if a in vowel:
            v_count.append(line.count(a))
        else:
            c_count.append(line.count(a))
    
    total_c = sum(c_count)
    total_v = sum(v_count)
    max_v = max(v_count)
    max_c= max(c_count)

    result = []
    min_c = total_v + (2*(total_c - max_c))
    result.append(min_c)
    min_v = total_c + (2*(total_v - max_v))
    result.append(min_v)

    return min(result)
    
with open('input.txt','r') as inf:
    T = int(inf.readline())

    for x in range(1,T+1):
        line = inf.readline().strip()
        result = min_time(line)
        with open('output.txt', 'a') as outf:
             outf.write('Case #{}: {}\n'.format(x,result))