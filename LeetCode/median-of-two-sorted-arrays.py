class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        k = 0
        x = len(nums1)+len(nums2)
        out = [0]*x
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                out[k] = nums1[i]
                i+=1
            else:
                out[k] = nums2[j]
                j+=1
            k+=1
        while i < len(nums1):
            out[k] = nums1[i]
            i+=1
            k+=1
        while j < len(nums2):
            out[k] = nums2[j]
            j+=1
            k+=1
        median = 0
        if x % 2 == 0:
            median = (out[x//2]+out[(x//2)-1])/2
        else:
            median = out[(x-1)//2]
        return float(median)
