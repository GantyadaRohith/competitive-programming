class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        j1 = m-1
        j2 = n-1
        k = len(nums1)-1
        while j1 >= 0 and j2 >= 0:
            if nums1[j1] > nums2[j2]:
                nums1[k] = nums1[j1]
                j1 -= 1
            else:
                nums1[k] = nums2[j2]
                j2 -= 1

            k -= 1
        while j2 >= 0:
            nums1[k] = nums2[j2]
            j2 -= 1
            k -= 1