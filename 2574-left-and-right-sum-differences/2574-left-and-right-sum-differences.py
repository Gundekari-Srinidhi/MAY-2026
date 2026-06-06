class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [] 
        val1 = sum(nums) - nums[0]
        res.append(val1)
        val = 0
        for i in range(1,n):
            val+=nums[i-1]
            val1 -= nums[i]
            res.append(abs(val - val1))
        return res
        





        