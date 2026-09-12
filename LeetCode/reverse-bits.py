class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(format(n,'032b'))
        x = x[::-1]
        x = int(x,2)
        return x
