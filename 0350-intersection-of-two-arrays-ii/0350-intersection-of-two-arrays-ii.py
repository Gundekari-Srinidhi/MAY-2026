class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l  = []
        n = len(nums1)
        m = len(nums2)
        for i in nums1:
            if i in nums2:
                l.append(i)
                nums2.remove(i)
        return l
        