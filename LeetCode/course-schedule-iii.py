class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        time_taken = 0
        cnt = 0
        mindur = []
        for d,l in courses:
            time_taken +=d
            heapq.heappush(mindur,-d)
            cnt+=1
            if time_taken>l:
                time_taken-=(-heapq.heappop(mindur))
                cnt-=1
        return cnt