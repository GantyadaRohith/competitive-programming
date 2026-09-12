class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        x1,y1 = start
        x2,y2 = target
        if (x1+y1)%2 == 0:
            if (x2+y2)%2 == 0:
                return True
            else:
                return False
        
        else:
            if (x2+y2)%2 != 0:
                return True
            else:
                return False 