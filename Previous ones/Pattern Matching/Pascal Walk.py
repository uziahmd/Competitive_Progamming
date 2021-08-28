def calc(N):
  sum =1
  n=1
  while True:
     n =n+1
     sum += n
     if  (sum >= N):
         break   
  sum-=n
  n-=1
  left = N - sum -1
  return left, n

T = int(input()) 
for t in range(1, T + 1):
    N =int(input())
    result = calc(N)
    print("Case #{}:".format(t))
    print("{} {}".format(1,1))
    if N > 1:
      for a in range(result[1]):
        print("{} {}".format(a+2, 2))
    if result[0] > 0:
       for i in range(result[0]):
          print("{} {}".format(result[1]+i,1))
