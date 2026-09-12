class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        if all(num % 2 != 0 for num in digits):
            return 0
            
        s = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            num = digits[i] * 100 + digits[j] * 10 + digits[k]
                            s.add(num)    
        return len(s)
