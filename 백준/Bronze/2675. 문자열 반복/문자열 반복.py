t = int(input())

for _ in range(t):
    cnt,word = input().split()
    for x in word:
        print(x*int(cnt), end="")
    print()