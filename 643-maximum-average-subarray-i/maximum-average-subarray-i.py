class Solution(object):
    def findMaxAverage(self, nums, k):
        c=sum(nums[:k])
        m=c
        for i in range(k,len(nums)):
            c+=nums[i]-nums[i-k]
            m=max(m,c)
        return m/float(k)
        