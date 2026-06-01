class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max1=0
        zero=0
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]==0:
                zero+=1
            while zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            t=r-l+1
            max1=max(max1,t)
        return max1
        