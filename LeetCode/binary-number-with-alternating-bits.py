class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        cnt = 0
        for i in s:
            if cnt!=1 and i == '1':
                cnt +=1
            elif cnt == 1 and i == '1':
                return False
            elif cnt!=0 and i == '0':
                cnt-=1
            elif cnt == 0 and i == '0':
                return False
        return True