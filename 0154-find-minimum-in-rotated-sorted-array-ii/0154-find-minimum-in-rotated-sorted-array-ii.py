class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        r = 1
        val = nums[0]
        while r < n:
            while r < n and nums[r] >= nums [r-1]:
                r+=1
            if r < n:
                val = nums[r]
                break
        return val