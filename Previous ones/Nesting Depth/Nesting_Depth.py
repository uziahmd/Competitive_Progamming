
def fun(S):
    previous = 0
    NewS = ''
    for i in range(len(S)):
        num = int(S[i])
        diff = num -previous
        if diff== 0:
            NewS += S[i]
        elif diff>0:
            NewS += diff * '(' + S[i]
        else:
            NewS += (-diff) *')' + S[i]
        previous = num

    if previous>0:
        NewS+= previous*')'
    return NewS

T = int(input())
for t in range(1,T+1):
    S = input()
    NewS = fun(S)
    print("Case #{}: {}".format(t, NewS))
