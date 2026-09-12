class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums1)

        for i in range(len(nums1)):
            f = -1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    f+=1
                if f == 0:
                    if nums1[i] < nums2[j]:
                        result[i]  = nums2[j]
                        break
        return result
