t = int(input())

for _ in range(t):
    n = int(input())
    a = {1: 0, 2: 0}
    te = list(map(int, input().split()))

    for i in te:
        a[i] = a.get(i, 0) + 1

    if a[2] == 0:
        print(1)

    elif a[2] & 1:
        print(-1)

    else:
        temp = a[2] // 2

        for i in range(n):
            if te[i] == 2:
                temp -= 1

            if temp == 0:
                print(i + 1)
                break 