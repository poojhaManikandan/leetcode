class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        c=0
        l=0
        r=len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            if sum==k:
                r=r-1
                c=c+1
                l=l+1
            elif sum>k:
                r=r-1
            else:
                l=l+1
        return c
            
        