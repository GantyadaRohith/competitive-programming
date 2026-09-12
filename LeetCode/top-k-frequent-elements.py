class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        out = [];x = 0
        d = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        for val,q in d.items():
            out.append(val)
            x+=1
            if x == k:
                break
        return out