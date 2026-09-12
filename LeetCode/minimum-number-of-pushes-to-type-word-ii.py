class Solution:
    def minimumPushes(self, word: str) -> int:
        x = {}
        pq = []
        for i in word:
            x[i] = x.get(i,0) + 1
        for ch,freq in x.items():
            heapq.heappush(pq,(-freq,ch))
        print(pq)
        count = 0
        i = 1
        while pq:
            freq,ch = heapq.heappop(pq)
            x[ch] = i
            count+=1
            if count == 8:
                i+=1
                count = 0
        print(x)
        res = 0
        for i in word:
            res += x[i]
        return res