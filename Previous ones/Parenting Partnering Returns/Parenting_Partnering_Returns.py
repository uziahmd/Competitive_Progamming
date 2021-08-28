def f(arrayin):
    arr = []
    for i in range(len(arrayin)):
        arr.append((arrayin[i][0], arrayin[i][1], i))
    arr.sort()
    Cend = 0
    Jend = 0
    a_sch = []
    for start, end, idx in arr:
        if start < Cend and start < Jend:
            return "IMPOSSIBLE"
        if start >= Cend:
            a_sch.append(('C', idx))
            Cend = end
        else:
            a_sch.append(('J', idx))
            Jend = end
    sch = ''
    for c, idx in sorted(a_sch, key=lambda x: x[1]):
        sch += c
    return sch

T = int(input()) 
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        interval = [int(s) for s in input().split(" ")]
        arr.append(interval)
    sch = f(arr)
    print("Case #{}: {}".format(t, sch))