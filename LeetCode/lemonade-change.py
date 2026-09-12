class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x,y,z = 0,0,0
        if bills[0] != 5:
            return False
        for i in bills:
            if i == 5:
                x+=1
            elif i == 10:
                if x >= 1:
                    x-=1
                    y+=1
                else:
                    return False
            elif i == 20:
                if y >= 1 and x >= 1:
                    y-=1
                    x-=1
                elif x >= 3:
                    x-=3
                else:
                    return False
            
        return True