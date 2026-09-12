n = int(input())
test = []
for _ in range(n):
    test.append(list(map(int,input().split())))
for i in range(len(test)):
    if test[i][0] > test[i][1]:
        print("First")
    elif test[i][0] == test[i][1] and test[i][2]&1:
        print("First")
    else:
        print("Second")