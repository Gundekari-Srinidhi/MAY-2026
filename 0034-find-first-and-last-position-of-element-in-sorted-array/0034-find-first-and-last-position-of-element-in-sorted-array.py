class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ans=[-1,-1]
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>=target:
                ans[0]=mid
                h=mid-1
            else:
                l=mid+1
        if ans[0]==-1 or ans[0]>=n or nums[ans[0]]!=target:
            ans[0]=-1
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]<=target:
                ans[1]=mid
                l=mid+1
            else:
                h=mid-1
        if ans[1]==-1 or nums[ans[1]]!=target:
            ans[1]=-1
        return ans
                

        