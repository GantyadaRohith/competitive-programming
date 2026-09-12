class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = abs((ax2-ax1)*(ay2-ay1))
        rect2= abs((bx2-bx1)*(by2-by1))
        overlap_h,overlap_w = 0,0
        overlap_area = 0
        if min(ax2,bx2)>max(ax1,bx1):
            overlap_h = min(ax2,bx2)-max(ax1,bx1)  
        if min(ay2,by2) > max(ay1,by1):
            overlap_w = min(ay2,by2)-max(ay1,by1)
        if overlap_h <= 0 or overlap_w <= 0:
            return rect1+rect2
        overlap_area = overlap_h*overlap_w
        return rect1+rect2-overlap_area