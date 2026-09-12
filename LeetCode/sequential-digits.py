class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        x = '123456789'
        i,j = len(str(low)),len(str(high))
        out = []
        k = min(i,j)
        while k <= max(i,j) :
            print(k)
            l = 0
            while l <= len(x)-k:
                if int(x[l:l+k])>=low and int(x[l:l+k]) <= high:
                    out.append(int(x[l:l+k])) 
                l+=1
            k+=1
        return out