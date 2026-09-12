class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        end = -inf
        cnt = 0

        for s,e in intervals:
            if s>=end:
                cnt+=1
                end = e
        return len(intervals)-cnt