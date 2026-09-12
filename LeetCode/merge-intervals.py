class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda person: person[0])
        print(intervals)
        out = []
        i = 0
        while i < (len(intervals)):
            if out and out[-1][1] >= intervals[i][0] :
                k,l = out.pop()
                m,n = intervals[i]
                out.append([min(k,m),max(l,n)])
                i+=1
                print(out)
            else:
                k,l = intervals[i]
                out.append([k,l])
                i+=1
        return out