class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        prefix=1
        for i in range(0,len(nums)):
            l.append(prefix)
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            l[i]*=suffix
            suffix*=nums[i]
        return l
            