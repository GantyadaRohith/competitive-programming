weight = int(input())
if (weight%2) != 0 or weight<=2:
    print("NO")
else:
    flag = 0
    for i in range(1,weight):
        if i%2 == 0 and (weight-i)%2 == 0:
            flag = 1
            break

    if flag:
        print("YES")
    else:
        print("NO")
