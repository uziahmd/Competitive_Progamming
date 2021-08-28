
def time(X,Y,M):
    for a in range(len(M)):
        if M[a]=='N':
            Y=Y+1
        elif M[a]=='S':
            Y=Y-1
        elif M[a]=='E':
            X=X+1
        elif M[a]=='W':
            X=X-1
        total = abs(X)+abs(Y)
        if (total <=a+1):
            return a+1
    return 'IMPOSSIBLE'

T = int(input())
for t in range(1, T+1):
    X, Y, M = [s for s in input().split(" ")]
    X = int(X)
    Y = int(Y)
    result = time(X, Y, M)
    print("Case #{}: {}".format(t,result))
