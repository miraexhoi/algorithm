n = int(input())
a = 1

for i in range(n-1,-1,-1):
    print(" "*i+"*"*a)
    a += 1