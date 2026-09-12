class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        out = []
        min_diff = float('inf')
        for i in range(0,len(arr)-1,1):
            diff = arr[i+1] - arr[i]
            min_diff = min(diff,min_diff)
        for i in range(0,len(arr)-1,1):
            if arr[i+1] - arr[i] == min_diff:
                out.append([arr[i],arr[i+1]])
        return out