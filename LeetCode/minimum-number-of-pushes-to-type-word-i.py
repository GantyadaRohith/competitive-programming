class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        n = len(word)
        if n<=8:
            return n
        elif n<=16:
            print(n-8)
            print(2*(n-8))
            return 8+2*(n-8)
        elif n<=24:
            return 8+2*8+3*(n-16)
        else:
            return 8+2*8+3*8+4*(n-24)