class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr,k):
            l,r = 0,len(arr)-1
            while(l<=r):
                mid = l+((r-l)//2)
                if arr[mid] == k:
                    return True
                elif arr[mid] > k:
                    r = mid-1
                else:
                    l = mid+1
            return False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return search(matrix[i],target)
        return False
 
        