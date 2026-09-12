class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        if n == 1:
            return s
        cst  = s
        res = ''
        st = '9876543210'
        i = 0
        while True:
            if cst>=int(st[i]):
                cst-=int(st[i])
                res+=st[i]
            else:
                i+=1
            if len(res) == n:
                break
        return int(res)