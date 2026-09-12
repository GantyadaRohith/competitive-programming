class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        out = []
        for i in trips:
         ppl,fro,to = i[0],i[1],i[2]
         out.append([fro,ppl])
         out.append([to,-ppl])
        out.sort()
        curr = 0
        possible = 1 
        for loc,ppl in out:
            curr+=ppl
            if curr > capacity:
                possible = 0
                break
        return False if possible == 0 else True