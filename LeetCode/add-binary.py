class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)!=len(b):
            if len(a) < len(b):
                a = '0'*(len(b)-len(a))+a
            else:
                b = '0'*(len(a)-len(b))+b
        def bitwise_add(a: str, b: str) -> str:
            # 1. Convert binary strings to integers (base 2)
            num1 = int(a, 2)
            num2 = int(b, 2)

            # 2. Apply the same bitwise addition logic
            while num2 != 0:
                sum_without_carry = num1 ^ num2
                carry = (num1 & num2) << 1
                num1 = sum_without_carry
                num2 = carry

            # 3. Convert back to binary string and strip the '0b' prefix
            return bin(num1)[2:]
        return bitwise_add(a,b)