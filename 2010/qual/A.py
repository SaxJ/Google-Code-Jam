N = int(input())

for c in range(N):
    credit = int(input())
    nItems = int(input())
    items = [int(x) for x in input().split(' ')]
    seen = {}
    for i, n in enumerate(items):
        if n in seen:
            print("Case #{}: {} {}".format(c+1, seen[n]+1, i+1))
            break

        r = credit - n
        seen[r] = i
