class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = defaultdict(int)
        for i in tasks:
            x[i] = x.get(i,0) + 1
        maxFreq = max(x.values())
        cnt_max = 0
        for i in x.values():
            if i == maxFreq:
                cnt_max+=1
        return max(sum(x.values()),(maxFreq-1)*(n+1)+cnt_max)