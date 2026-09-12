class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 2:
            return 2
        elif len(points) == 1:
            return 1
        else:
            result = 1
            for i in range(len(points)):
                x1,y1 = points[i]
                for j in range(i+1,len(points)):
                    x2,y2 = points[j]
                    cnt = 2
                    for k in range(j+1,len(points)):
                        x3,y3 = points[k]
                        if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                            cnt+=1
                    result = max(cnt,result)
            return result