class Solution:
    def isHappy(self, n: int) -> bool:
        if n<9 and (n ==1 or n == 7):
            return True
        else:
            while len(str(n))!=1:
                count = 0
                for i in str(n):
                    count+=(int(i)**2)
                n = count
            if n<9 and (n ==1 or n == 7):
                return True
            else:
                return False
        