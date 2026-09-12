class Solution:
    def minOperations(self, s: str) -> int:
        op1 = 0
        op2 = 0

        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                op1 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                op2 += 1

        return min(op1, op2)