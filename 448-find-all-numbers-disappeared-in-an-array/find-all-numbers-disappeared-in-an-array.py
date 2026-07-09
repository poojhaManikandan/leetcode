class Solution(object):
    def findDisappearedNumbers(self, nums):
        num=set(nums)
        m=len(nums)
        res=[]
        for i in range(1,m+1):
            if i not in num:
                res.append(i)
        return res
