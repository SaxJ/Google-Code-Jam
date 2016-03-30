N = int(input())
for i in range(N):
    words = input().split(' ')
    rev = list(reversed(words))
    print("Case #{}: {}".format(i+1, ' '.join(rev)))
