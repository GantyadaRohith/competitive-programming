class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) !=1 :
            rem=0
            sum=0
            while num >0:
                rem=num%10
                sum+=rem
                num//=10
            return self.addDigits(sum)
        else:
            return num