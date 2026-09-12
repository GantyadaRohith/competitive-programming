class Solution:
    def minSwaps(self, s: str) -> int:
        b = 0
        ib = 0
        st = list(s)
        for i in st:
            if i == '[':
                b+=1
            else:
                if b > 0:
                    b-=1
                else:
                    ib+=1
        return (ib+1)//2