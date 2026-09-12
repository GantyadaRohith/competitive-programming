class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        s = ""

        while num:
            if num & 1:
                s += "0"
            else:
                s += "1"
            num >>= 1

        s = s[::-1]
        return int(s, 2)