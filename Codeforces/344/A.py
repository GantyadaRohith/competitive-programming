t = int(input())
arr = []
for _ in range(t):
    arr.append(input())
cnt = 1
temp = ''
for i in range(1,len(arr)):
    if arr[i-1] != arr[i]:
        cnt+=1

print(cnt)