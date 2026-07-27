class Solution(object):
    def maxProduct(self, nums):
        lis=sorted(nums)
        m1=lis[-1]
        m2=lis[-2]
        return (m1-1)*(m2-1)