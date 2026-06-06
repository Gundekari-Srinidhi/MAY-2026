class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lf = [0]
        val = nums[0]
        lf.append(val)
        for i in range(2,n):
            val+=nums[i-1]
            lf.append(val)
        rf = []
        val = sum(nums) - nums[0]
        rf.append(val)
        for i in range(1,n):
            val -= nums[i]
            rf.append(val)
        res = []
        for i in range(n):
            res.append(abs(lf[i]-rf[i]))
        return res
        





        