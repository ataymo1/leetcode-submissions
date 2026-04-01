class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1, p2 = 0, 0
        p3 = 0
        nums1_copy = nums1[:]

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p3] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p3] = nums2[p2]
                p2 += 1
            p3 += 1
        
        if p1 < m:
            for i in range(p3, len(nums1)):
                nums1[i] = nums1_copy[p1]
                p1 += 1
        elif p2 < n:
            for i in range(p3, len(nums1)):
                nums1[i] = nums2[p2]
                p2 += 1





        