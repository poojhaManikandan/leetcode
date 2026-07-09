class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)

        index = {}

        for i, num in enumerate(sorted_nums):
            if num not in index:
                index[num] = i

        return [index[num] for num in nums]
        
            