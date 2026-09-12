class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        out = []
        odd = []
        eve = []
        for i in nums:
            if i < 0:
                odd.append(i)
            else:
                eve.append(i)
        x = y = 0
        for i in range(len(odd)+len(eve)):
            if i%2==0 and x < len(eve):
                out.append(eve[x])
                x+=1
            elif i%2!= 0 and y<len(odd):
                out.append(odd[y])
                y+=1
            else:
                continue
        return out