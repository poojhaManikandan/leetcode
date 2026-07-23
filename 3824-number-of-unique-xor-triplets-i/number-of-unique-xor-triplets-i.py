class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)        
        return 1 << (n.bit_length() - 3 // (n + 1))
        