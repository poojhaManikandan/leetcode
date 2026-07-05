class Solution(object):
    def twoSum(self, nums, target):
        pair={}
        for i,num in enumerate(nums):
            if target-num in pair:
                return [i,pair[target-num]]
            pair[num]=i
        

        