t = int(input())
for _ in range(t):
    rat = input()
    if rat[0]!='-':
        rat = int(rat)
    else:
        rat = -1*int(rat[1:])
    if rat<=1399:
        print("Division 4")
    elif rat<=1599:
        print("Division 3")
    elif rat<=1899:
        print("Division 2")
    else:
        print("Division 1")